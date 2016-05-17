import random as rnd


def shuffle(deck):
    rnd.shuffle(deck)
    return deck


def get_deck():
    deck = []
    for suit in suits():
        for rank in ranks():
            deck.append(card(suit, rank))
    return deck


def card(suit, rank):
    return {
        'suit': suit,
        'rank': rank
    }


def suits():
    return [
        "Hearts",
        "Diamonds",
        "Spades",
        "Clubs"
    ]


def ranks():
    return [
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "J",
        "Q",
        "K",
        "A"
    ]
