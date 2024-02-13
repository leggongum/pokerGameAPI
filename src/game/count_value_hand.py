from functools import cache

combinations = {
    "straight-flush": (0 + 624 + 3744 + 5108 + 10200 + 54912 + 123552 + 1098240 + 1302540, 40),
    "four-of-a-kind": (0 + 3744 + 10200 + 5108 + 54912 + 123552 + 1098240 + 1302540, 624),
    "full house": (0 + 10200 + 5108 + 54912 + 123552 + 1098240 + 1302540, 3744),
    "flush": (0 + 10200 + 54912 + 123552 + 1098240 + 1302540, 5108),
    "straight": (0 + 54912 + 123552 + 1098240 + 1302540, 10200),
    "three-of-a-kind": (0 + 123552 + 1098240 + 1302540, 54912),
    "two pair": (0 + 1098240 + 1302540, 123552),
    "pair": (0 + 1302540, 1098240),
    "nothing": (0, 1302540),
    }

all_combinations = 2598960


@cache
def count_value_combination(combination, cards) -> int:
    wins, possible_wins = combinations[combination]

    if combination[:8] == "straight" or combination == "four-of-a-kind":
        outs = 13 if combination == "four-of-a-kind" else 10
        for n, card in enumerate(('A','K','Q','J','10','9','8','7','6','5','4','3','2'), 1):
            if card == cards[0]:
                return wins + possible_wins*((outs-n)//outs)
    

    elif combination == "full house":
        not_win = 0
        variants = ['A','K','Q','J','10','9','8','7','6','5','4','3','2']
        for card1 in variants:
            if cards[0] == card1:
                possible_combinations = variants.copy()
                possible_combinations.remove(card1)
                for card2 in possible_combinations:
                    not_win -= 24
                    if cards[1] == card2:
                        return wins + possible_wins + not_win
            not_win -= 288

    elif combination == "flush" or combination == "nothing":
        # Сложно посчитать, сколько именно флешей бьёт конкретный флеш
        # => Костыль: сила флеша равна сумме сил карт 
        # Сила карты = два в степени значения карты (чтобы избежать коллизий)
        # Та же ситуация со старшей(ими) картой(ами)
        # (1277 рук упаковал в 8192 чисел)

        pow_ = 12
        sum_ = 0
        for card in ('A','K','Q','J','10','9','8','7','6','5','4','3','2'):
            if card in cards:
                sum_ += 2**pow_
            pow_ -= 1
        return wins + int(possible_wins * (sum_ / (4096+2048+1024+512+128))) - 1
    
    elif combination in ("three-of-a-kind", "two pair"):
        # 54912 = 13 * 12 * 11 * 32(?) "three-of-a-kind"
        # 123552 = 13 * 12 * 11 * 72(?) "two pair"
        not_win = 0
        step_map = [4224, 352, 32] if combination == "three-of-a-kind" else [9504, 792, 72]
        variants = ['A','K','Q','J','10','9','8','7','6','5','4','3','2']
        for card1 in variants:
            if cards[0] != card1:
                not_win -= step_map[0]
                continue
            possible_combinations_kicker1 = variants.copy()
            possible_combinations_kicker1.remove(card1)
            for card2 in possible_combinations_kicker1:
                if cards[1] != card2:
                    not_win -= step_map[1]
                    continue
                possible_combinations_kicker2 = possible_combinations_kicker1.copy()
                possible_combinations_kicker2.remove(card2)
                for card3 in possible_combinations_kicker2:
                    not_win -= step_map[2]
                    if cards[2] == card3:
                        return wins + possible_wins + not_win
    
    elif combination == "pair":
        # 84480 * 7040 * 640 * 64
        # 1098240 = 13 * 12 * 11 * 10 * 64(?)
        not_win = 0
        variants = ['A','K','Q','J','10','9','8','7','6','5','4','3','2']
        for card1 in variants:
            if cards[0] != card1:
                not_win -= 84480
                continue
            possible_combinations_kicker1 = variants.copy()
            possible_combinations_kicker1.remove(card1)
            for card2 in possible_combinations_kicker1:
                if cards[1] != card2:
                    not_win -= 7040
                    continue
                possible_combinations_kicker2 = variants.copy()
                possible_combinations_kicker2.remove(card2)
                for card3 in possible_combinations_kicker2:
                    if cards[2] != card3:
                        not_win -= 640
                        continue
                    possible_combinations_kicker3 = variants.copy()
                    possible_combinations_kicker3.remove(card3)
                    for card4 in possible_combinations_kicker3:
                        not_win -= 64
                        if cards[3] == card4:
                            return wins + possible_wins + not_win
            
    print(combination, cards)
    return f'win: {0}, tie: {0}'
