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


def sort_cards(cards):
    return sorted(
        cards, key=lambda card: - ranks.index(card[1])
    )

def gen_cards(n=7):
    if n > 52:
        raise ValueError(f"You can only draw up to 52 cards. You requested {n}")
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

    return random.sample(deck, n)


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
        
        if straight_cards:
            previous_card = straight_cards[-1]
            previous_place = ranks.index(previous_card[1])
        else:
            previous_place = None

        # No cards found for straight; so add this one to the list to get started.
        if len(straight_cards) == 0:
            straight_cards.append(card)
        
        # Same rank, keep first card found.
        elif previous_place == place: 
            continue
        
        # Card is one rank below previous card
        elif previous_place == place + 1:
            straight_cards.append(card)
        
        # Unable to add card on this iteration and impossible to find straight
        # with remaining cards.
        elif iter_number >= 2 and len(straight_cards) < 5:
            return None
        
        # Still possible to find straight, but will need to look at remaining
        # cards.
        elif len(straight_cards) < 5:
            straight_cards = []
            
    if len(straight_cards) >= 5:
        return straight_cards
    
    return None


def choose_cards(cards):
    cards = sort_cards(cards)

    # Royal Flush
    royal_flush = get_royal_flush(cards)
    if royal_flush is not None:
        return ("royal_flush", sort_cards(royal_flush))

    # ...other hands will go here when they are implemented.
    
    # Flush
    flush = get_flush(cards)

    if flush is not None:
        straight_flush = get_straight(flush)
        if straight_flush is not None:
            return ("straight_flush", sort_cards(straight_flush[:5]))

    if flush is not None:
        return ("flush", sort_cards(flush[:5]))

    straight = get_straight(cards)

    if straight is not None:
        return ("straight", sort_cards(straight))

    return None
