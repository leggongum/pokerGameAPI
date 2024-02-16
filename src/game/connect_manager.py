from starlette.websockets import WebSocket
from pydantic import BaseModel, ConfigDict

import asyncio
from typing import Literal
from random import shuffle, randint

from game.combination import hand
from game.count_value_hand import count_value_combination


class Player(BaseModel):
    id: str
    name: str
    ws: WebSocket
    chips_amount: int = 100
    message: str | None = None
    bet: int = 0
    cards: list[str] = []
    is_in_game: bool = False
    max_winnings: int = 0

    model_config = ConfigDict(arbitrary_types_allowed=True)

    def __repr__(self):
        return f'{self.id}, {self.name}, {self.ws}'


class ConnectionManager:
    current_active_lobbies = {}

    def __init__(self, lobby_title: str):
        self.lobby_title = lobby_title
        self.players: list[Player] = []
        self.game_phase: Literal['wait', 'preflop', 'flop', 'turn', 'river'] = 'wait'
        self.bank: int = 0
        self.turn = None
        self.is_running = False
        self.call_and_check_count: int = 0
        self.max_bet: int = 0
        self.action: dict|None = None
        self.event = asyncio.Event()
        self.cards: list[str] = []
        self.deck: list[str] = [value + suit for suit in ['♠','♦','♣','♥'] for value in ['A','K','Q','J','10','9','8','7','6','5','4','3','2']]
        shuffle(self.deck)
        self.unavailable_cards = set()
        ConnectionManager.current_active_lobbies[lobby_title] = self
        print(ConnectionManager.current_active_lobbies)


    async def connect(self, websocket: WebSocket, user_id, user_name):
        await websocket.accept()
        self.players.append(Player(id=user_id, name=user_name, ws=websocket, chips_amount=100, is_in_game=False))
        print(self.players)
        if len(self.players) > 1 and not self.is_running:
            self.turn = self.players[0]
            asyncio.create_task(self.game_process(0))


    def disconnect(self, websocket: WebSocket):
        for player in self.players:
            if player.ws == websocket:
                self.players.remove(player)
                break


    @staticmethod
    def get_stadies():
        stadies = ['preflop', 'flop', 'turn', 'river']
        i = 0
        while True:
            yield stadies[i%4]
            i = i + 1
    

    def count_active_players(self) -> int:
        count = 0
        for player in self.players:
            if player.is_in_game:
                count += 1
        return count


    async def check_call(self):
        if self.max_bet == self.turn.bet:
            await self.send_update_in_lobby({'type': 'check', 'from': self.turn.name})
        else:
            if self.turn.bet + self.turn.chips_amount >= self.max_bet:
                need = self.max_bet - self.turn.bet
                self.turn.bet = self.max_bet
                self.turn.chips_amount -= need
                self.bank += need
            else:
                self.turn.bet += self.turn.chips_amount
                self.turn.chips_amount = 0
                self.bank += self.turn.chips_amount
            await self.send_update_in_lobby({'type': 'call', 'from': self.turn.name, 
                                             'bet': self.turn.bet, 
                                             'chips': self.turn.chips_amount})
        self.call_and_check_count += 1


    async def pass_(self):
        self.turn.is_in_game = False
        await self.send_update_in_lobby({'type': 'pass', 'from': self.turn.name})


    async def raise_(self, amount):
        if amount > self.turn.chips_amount:
            amount = self.turn.chips_amount
        self.turn.bet += amount
        self.bank += amount
        self.max_bet += amount
        self.turn.chips_amount -= amount

        await self.send_update_in_lobby({'type': 'raise', 'amount': amount, 'bet': self.turn.bet, 'chips': self.turn.chips_amount, 'from': self.turn.name})
        self.call_and_check_count = 1


    async def make_simple_turn(self):
        if self.turn.bet == self.max_bet or self.turn.chips_amount < 1:
            await self.check_call()
        else:
            await self.pass_()

    
    async def show_cards(self, player: Player):
        await self.send_update_in_lobby({'type': 'show cards', 'content': player.cards})
    


    async def reveal_the_cards(self):
        player_cards_map = {}
        player_value_list = []
        for player in self.players:
            if player.is_in_game:
                player_cards_map[player.name] = player.cards
                player_value_list.append((player, count_value_combination(*hand(tuple(player.cards + self.cards)))))

        for player in self.players:
            player.max_winnings = sum(min(player.bet, p.bet) for p in self.players)

        player_value_list.sort(key=lambda x: x[1], reverse=True)
        group = []
        value = float('inf')
        for player, v in player_value_list:
            if not self.bank: break
            if v < value:
                if group:
                    group.sort(key=lambda p: p.max_winnings)
                    number_winners = len(group)
                    for player in group:
                        player.chips_amount += player.max_winnings // number_winners
                        self.bank -= player.max_winnings // number_winners
                        number_winners -= 1
                    if not self.bank:
                        break
                    group = [player]
                else:
                    group.append(player)
            else:
                group.append(player)
        
        await self.send_update_in_lobby({'type': 'final', 'players_cards': player_cards_map})
        

    async def get_turn(self):
        await self.turn.ws.send_json({'type': 'get_turn'})

        await self.event.wait()
        print(f'Response get_turn: {self.action}')

        response = self.action
        action = response['action']
        if action == 'check-call':
            await self.check_call()
        elif action == 'raise':
            await self.raise_(response['amount'])
        elif action == 'pass':
            await self.pass_()



    def get_next_index_player(self, indx_player):
        indx_player += 1
        if indx_player >= len(self.players):
            indx_player = 0
        while not self.players[indx_player].is_in_game:
            indx_player += 1
            if indx_player >= len(self.players):
                indx_player = 0
        return indx_player


    async def game_process(self, indx_player: int):
        self.is_running = True
        print('start game')


        active_players_counter = 0
        limit = 23
        for player in self.players:
            if player.chips_amount > 0 and active_players_counter < limit:
                player.is_in_game = True
                active_players_counter += 1


        get_stadies = ConnectionManager.get_stadies()
        phase_func_map = {'preflop': self.send_preflop_info, 
                          'flop': self.send_flop_info, 
                          'turn': self.send_turn_info, 
                          'river': self.send_river_info}
        next_index_player = indx_player
        while self.count_active_players() > 1:
            self.game_phase = get_stadies.__next__()
            await phase_func_map[self.game_phase]()
            self.call_and_check_count = 0
            while self.count_active_players() > self.call_and_check_count: # пока не все check или call, ход передаётся следующему
                print(self.count_active_players(), self.call_and_check_count)
                await asyncio.sleep(5)
                if self.turn.chips_amount > 0:
                    try:
                        await asyncio.wait_for(self.get_turn(), 60)
                    except asyncio.exceptions.TimeoutError:
                        await self.make_simple_turn()
                    self.event.clear()
                else:
                    self.call_and_check_count += 1
                next_index_player = self.get_next_index_player(next_index_player)

                self.turn = self.players[next_index_player]
                if self.count_active_players() == 1:
                    self.players[next_index_player].chips_amount += self.bank
                    self.max_bet = 0
                    self.bank = 0
                    break

            if self.game_phase == 'river' and self.count_active_players() > 1: # Если дошли до ривера, все активные игроки вскрывают карты
                await self.reveal_the_cards()
                self.max_bet = 0
                self.bank = 0
                await asyncio.sleep(10)
        if len(self.players) > 1:
            indx_player = self.get_next_index_player(indx_player)
            await self.game_process(indx_player)
        self.is_running = False


    async def send_update_in_lobby(self, message: dict):
        for player in self.players:
            await player.ws.send_json(message)


    def get_cards_from_deck(self, amount: int) -> list:
        cards = []
        for _ in range(amount):
            number = randint(0, 51)
            while number in self.unavailable_cards: 
                number = randint(0, 51)
            self.unavailable_cards.add(number)
            cards.append(self.deck[number])
        return cards


    async def send_preflop_info(self):

        self.max_bet = 10

        for n, player in enumerate(self.players):
            if n == len(self.players) -1:
                player.chips_amount = max(player.chips_amount - 10, 0)
                player.bet = 10
            else:
                player.chips_amount = max(player.chips_amount - 5, 0)
                player.bet = 5
            player.cards = self.get_cards_from_deck(2)
            await player.ws.send_json({'type': 'info',
                                    'stage': 'preflop', 
                                    'self_cards': player.cards, 
                                    'chips': player.chips_amount,
                                    'bet': player.bet})


    async def send_flop_info(self):
        self.cards = self.get_cards_from_deck(3)
        for player in self.players:
            await player.ws.send_json({'type': 'info',
                                       'stage': 'flop', 
                                    'self_cards': player.cards, 
                                    'chips': player.chips_amount,
                                    'bet': player.bet,
                                    'board_cards': self.cards})
            

    async def send_turn_info(self):
        self.cards += self.get_cards_from_deck(1)
        for player in self.players:
            await player.ws.send_json({'type': 'info',
                                       'stage': 'turn', 
                                    'self_cards': player.cards, 
                                    'chips': player.chips_amount,
                                    'bet': player.bet,
                                    'board_cards': self.cards})


    async def send_river_info(self):
        self.cards += self.get_cards_from_deck(1)
        for player in self.players:
            await player.ws.send_json({'type': 'info',
                                       'stage': 'river', 
                                    'self_cards': player.cards, 
                                    'chips': player.chips_amount,
                                    'bet': player.bet,
                                    'board_cards': self.cards})


def get_manager(lobby_title: str):
    if lobby_title in ConnectionManager.current_active_lobbies:
        return ConnectionManager.current_active_lobbies[lobby_title]
    return ConnectionManager(lobby_title)