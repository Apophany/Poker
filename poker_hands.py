import cards

NOTHING = "Nothing"
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
        NOTHING: 0,
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


def high_card(hand):
    return max(
        hand,
        key=lambda card: cards.ranking(card)
    )


def two_pair(hand):
    hand.sort(key=lambda card: cards.ranking(card))
    pair = None
    prev_card = {'rank': -1}
    for card in hand:
        if prev_card['rank'] == card['rank']:
            pair = [prev_card, card]
        prev_card = card
    return pair


def three_of_a_kind(hand):
    triplet = None
    if len(hand) < 3:
        return triplet

    hand.sort(key=lambda card: cards.ranking(card))
    i = 0
    while i < len(hand):
        first_card = hand[i]
        second_card = hand[i + 1]
        third_card = hand[i + 2]
        if first_card['rank'] == second_card['rank'] == third_card['rank']:
            triplet = [first_card, second_card, third_card]
        i += 3
    return triplet
