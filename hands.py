import cards

HIGH_CARD = "High Card"
ONE_PAIR = "One Pair"
TWO_PAIR = "Two Pair"
THREE_OF_A_KIND = "Three of a Kind"
STRAIGHT = "Straight"
FLUSH = "Flush"
FULL_HOUSE = "Full House"
FOUR_OF_A_KIND = "Four of a Kind"
STRAIGHT_FLUSH = "Straight Flush"


def get_hand_ranks():
    return {
        HIGH_CARD: 1,
        ONE_PAIR: 2,
        TWO_PAIR: 3,
        THREE_OF_A_KIND: 4,
        STRAIGHT: 5,
        FLUSH: 6,
        FULL_HOUSE: 7,
        FOUR_OF_A_KIND: 8,
        STRAIGHT_FLUSH: 9
    }

