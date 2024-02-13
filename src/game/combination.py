class Poker:
    value_map = {r:v for r,v in zip(('A','K','Q','J','10','9','8','7','6','5','4','3','2'), range(2,15))}
    class Card:
        def __init__(self, card):
            self.rank = card[:-1]
            self.value = Poker.value_map[self.rank]
            self.suit = card[-1]
            
        def __hash__(self):
            return hash(self.rank)
    
    def __init__(self, cards):
        self.cards = sorted((Poker.Card(c) for c in cards), key=lambda x:x.value, reverse=True)
        self.rank_count = {r:0 for r in ('A','K','Q','J','10','9','8','7','6','5','4','3','2')}
        self.suit_count = {s:0 for s in '♠♦♣♥'}
        for card in self.cards:
            self.rank_count[card.rank] += 1
            self.suit_count[card.suit] += 1
        
    def best_hand(self):
        if hand:=self.four_of_a_kind():
            return ("four-of-a-kind", tuple(hand))
        elif hand:=self.full_house():
            return ("full house", tuple(hand))
        elif flush:=self.flush():
            if straight:=self.straight(flush):
                return ("straight-flush", tuple(straight))
            return ("flush", tuple([c.rank for c in flush[:5]]))
        elif straight:=self.straight(self.cards):
            return ("straight", tuple(straight))
        elif hand:=self.three_of_a_kind():
            return ("three-of-a-kind", tuple(hand))
        elif r1:=self.pair():
            if r2:=self.pair(r1[0]):
                return ("two pair", tuple([r1[0]]+r2))
            return ("pair", tuple(r1))
        else:
            return ("nothing", tuple([c.rank for c in self.cards[:5]]))
    
    def four_of_a_kind(self):
        for rank, count in self.rank_count.items():
            if count == 4:
                tie = None if not [c.rank for c in self.cards if c.rank != rank] else [c.rank for c in self.cards if c.rank != rank][0]
                return [rank, tie]
        return []
    
    def full_house(self):
        if three:=self.three_of_a_kind():
            r3 = three[0]
            if two:=self.pair(r3):
                r2 = two[0]
                return [r3,r2]
        return []
                
    
    def flush(self):
        for suit, count in self.suit_count.items():
            if count >= 5:
                return [card for card in self.cards if card.suit==suit]
        return []
    
    def straight(self, cards):
        cards = sorted(set(c.rank for c in cards), key=lambda x:self.value_map[x], reverse=True)
        if cards[0] == 'A' and cards[-1:-5:-1] == ['2','3','4','5']:
            return ['5', '4', '3', '2', 'A']
        for i in range(len(cards)-4):
            run = cards[i:i+5]
            if all(self.value_map[a]-self.value_map[b]==1 for a,b in zip(run, run[1:])):
                return run
        return []
    
    def three_of_a_kind(self):
        for rank, count in self.rank_count.items():
            if count == 3:
                tie = [c.rank for c in self.cards if c.rank != rank][:2]
                return [rank] + tie
        return []
    
    def pair(self, exclude=None):
        for rank, count in self.rank_count.items():
            if count >= 2:
                if exclude is not None:
                    if rank != exclude:
                        tie = [c.rank for c in self.cards if c.rank not in [rank, exclude]][0]
                        return [rank, tie]
                else:
                    tie = [c.rank for c in self.cards if c.rank != rank][:3]
                    return [rank]+tie
        return []


def hand(cards: tuple):
    poker = Poker(cards)
    return poker.best_hand()