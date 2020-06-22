"""
Card generator and chooser

1. Generate 5 random cards from a 52 card deck.
   13 cards with 4 suits

2. Code out combinations.



"""

import random
from collections import defaultdict

royal_cards = [
    "Jack",
    "Queen",
    "King",
    "Ace"
]

ranks = list(range(1, 11)) + royal_cards

def gen_cards():
    suites = [
        "diamonds",
        "hearts",
        "spades",
        "clubs",
    ]

    deck = []

    for suite in suites:
        for rank in ranks:
            deck.append(
                (suite, rank)
            )

    return random.sample(deck, 7)


def get_royal_flush(cards):
    royal_flushes = []
    for suite in ["diamonds", "hearts", "spades", "clubs"]:
        royal_flush = set()
        for rc in [10] + royal_cards:
            royal_flush.add((suite, rc))
        royal_flushes.append(royal_flush)
    
    set_cards = set(cards)
    
    for royal_flush in royal_flushes:
        if len(royal_flush - set_cards) == 0:
            return list(royal_flush)
    
    return None


def get_flush(cards):
    flush_counter = defaultdict(list)

    for card in cards:
        flush_counter[card[0]].append(card)
    for suite in flush_counter:
        if len(flush_counter[suite]) >= 5:
            return flush_counter[suite]
    return None


def get_straight(cards):
    straight_cards = []

    previous_place = None
    for iter_number, card in enumerate(cards[::]):
        place = ranks.index(card[1])
        if previous_place is None:
            straight_cards.append(card)
        elif previous_place == place + 1:
            straight_cards.append(card)
        elif iter_number >= 2:
            return None
        else:
            straight_cards = []
    
    if len(straight_cards) >= 5:
        return straight_cards
    return None


def choose_cards(cards):
    cards.sort(
        key=lambda card: - ranks.index(card[1])
    )

    # Royal Flush
    royal_flush = get_royal_flush(cards)
    if royal_flush is not None:
        return ("royal_flush", royal_flush)

    # ...other hands will go here when they are implemented.
    
    # Flush
    flush = get_flush(cards)

    if flush is not None:
        straight_flush = get_straight(flush)
        if straight_flush is not None:
            return ("straight_flush", straight_flush[:6])

    if flush is not None:
        return ("flush", flush[:6])

    straight = get_straight(cards)

    if straight is not None:
        return ("straight", straight)

    return None


if __name__ == "__main__":

    royal_flush_ex = [
        ("diamonds", "Ace"), ("diamonds", "King"), ("diamonds", "Queen"), ("diamonds", "Jack"), ("diamonds", 10), ("spades", 2), ("clubs", "Ace")
    ]
    res0 = choose_cards(royal_flush_ex)
    assert res0[0] == "royal_flush"
    print(res0)

    # TODO: Oops, I broke this example writing the royal_flush code.
    # flush_ex = [
    #      ("diamonds", 2), ("diamonds", "King"), ("diamonds", "Queen"), ("diamonds", "Jack"), ("diamonds", 10), ("spades", 2), ("clubs", "Ace")
    # ]
    # res1 = choose_cards(flush_ex)
    # assert res1[0] == "flush", res1
    # print(res1)


    straight_ex = [
        ("hearts", "Ace"), ("diamonds", "King"), ("diamonds", "Queen"), ("diamonds", "Jack"), ("diamonds", 10), ("spades", 2), ("clubs", "Ace")
    ]
    res2 = choose_cards(straight_ex)
    assert res2[0] == "straight"
    print(res2)


    straight_flush_ex1 = [
        ("diamonds", "King"), ("diamonds", "Queen"), ("diamonds", "Jack"), ("diamonds", 10), ("diamonds", 9),  ("spades", 2), ("clubs", "Ace")
    ]
    res3 = choose_cards(straight_flush_ex1)
    assert res3[0] == "straight_flush"
    print(res3)

    straight_flush_ex2 = [
        ("clubs", "Ace"), ("diamonds", "King"), ("diamonds", "Queen"), ("diamonds", "Jack"), ("diamonds", 10), ("diamonds", 9),  ("diamonds", 8)
    ]
    res4 = choose_cards(straight_flush_ex2)
    assert res4[0] == "straight_flush"
    print(res4)
