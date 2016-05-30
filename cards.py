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


def ranking(card):
    return ranks().index(card['rank'])
