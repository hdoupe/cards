import pytest

from cards import choose_cards, gen_cards


def test_gen_cards():
    # Test cards are unique and test using non-default hand sizes.
    for _ in range(1000):
        cards = gen_cards()
        assert len(cards) == len(set(cards)) == 7

    cards = gen_cards(52)
    assert len(cards) == len(set(cards)) == 52


    cards = gen_cards(12)
    assert len(cards) == len(set(cards)) == 12

def test_too_many_cards():
    with pytest.raises(ValueError):
        gen_cards(100)

def test_royal_flush():
    royal_flush_ex = [
        ("diamonds", "Ace"),
        ("diamonds", "King"),
        ("diamonds", "Queen"),
        ("diamonds", "Jack"),
        ("diamonds", 10),
        ("spades", 2),
        ("clubs", "Ace"),
    ]
    res = choose_cards(royal_flush_ex)
    assert res[0] == "royal_flush"
    assert res[1] == [
        ("diamonds", "Ace"),
        ("diamonds", "King"),
        ("diamonds", "Queen"),
        ("diamonds", "Jack"),
        ("diamonds", 10),
    ]


def test_flush():
    flush_ex = [
        ("diamonds", 2),
        ("diamonds", "King"),
        ("diamonds", "Queen"),
        ("diamonds", "Jack"),
        ("diamonds", 10),
        ("spades", 2),
        ("clubs", "Ace"),
    ]
    res = choose_cards(flush_ex)
    assert res[0] == "flush"
    assert res[1] == [
        ("diamonds", "King"),
        ("diamonds", "Queen"),
        ("diamonds", "Jack"),
        ("diamonds", 10),
        ("diamonds", 2),
    ]



def test_straight():
    straight_ex = [
        ("hearts", "Ace"),
        ("diamonds", "King"),
        ("diamonds", "Queen"),
        ("diamonds", "Jack"),
        ("diamonds", 10),
        ("spades", 2),
        ("clubs", "Ace"),
    ]
    res = choose_cards(straight_ex)
    assert res[0] == "straight"
    assert res[1] == [
        ("hearts", "Ace"),
        ("diamonds", "King"),
        ("diamonds", "Queen"),
        ("diamonds", "Jack"),
        ("diamonds", 10),
    ]

    straight_ex = [
        ("spades", 3),
        ("clubs", 2),
        ("hearts", "Ace"),
        ("diamonds", "King"),
        ("diamonds", "Queen"),
        ("diamonds", "Jack"),
        ("diamonds", 10),
    ]
    res = choose_cards(straight_ex)
    assert res[0] == "straight"
    assert res[1] == [
        ("hearts", "Ace"),
        ("diamonds", "King"),
        ("diamonds", "Queen"),
        ("diamonds", "Jack"),
        ("diamonds", 10),
    ]


def test_straight_flush1():
    straight_flush_ex1 = [
        ("diamonds", "King"),
        ("diamonds", "Queen"),
        ("diamonds", "Jack"),
        ("diamonds", 10),
        ("diamonds", 9),
        ("spades", 2),
        ("clubs", "Ace"),
    ]
    res = choose_cards(straight_flush_ex1)
    assert res[0] == "straight_flush"
    assert res[1] == [
        ("diamonds", "King"),
        ("diamonds", "Queen"),
        ("diamonds", "Jack"),
        ("diamonds", 10),
        ("diamonds", 9),
    ]


def test_straight_flush2():
    straight_flush_ex2 = [
        ("clubs", "Ace"),
        ("diamonds", "King"),
        ("diamonds", "Queen"),
        ("diamonds", "Jack"),
        ("diamonds", 10),
        ("diamonds", 9),
        ("diamonds", 8),
    ]
    res = choose_cards(straight_flush_ex2)
    assert res[0] == "straight_flush"
    assert res[1] == [
        ("diamonds", "King"),
        ("diamonds", "Queen"),
        ("diamonds", "Jack"),
        ("diamonds", 10),
        ("diamonds", 9),
    ]

