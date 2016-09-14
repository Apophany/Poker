import poker_hands
import cards as cards
import scipy.special as sp
import math as math


def hand_probabilities(hand, cards_remaining, cards_to_draw, table_cards=None):
    probabilities = {}
    for hand_rank in poker_hands.hand_ranks():
        if hand_rank is poker_hands.HIGH_CARD or hand_rank is poker_hands.NOTHING:
            continue

        probabilities[hand_rank] = calculate_prob(
            hand_rank,
            hand,
            cards_remaining,
            cards_to_draw
        )
    return probabilities


def calculate_prob(hand_rank, hand, cards_remaining, cards_to_draw):
    return {
        poker_hands.ONE_PAIR: one_pair_probability,
        poker_hands.TWO_PAIR: two_pair_probability,
        poker_hands.THREE_OF_A_KIND: three_of_a_kind_probability,
        poker_hands.STRAIGHT: straight_probability
    }.get(hand_rank, null_probability)(hand, cards_remaining, cards_to_draw)


def one_pair_probability(hand, cards_remaining, cards_to_draw):
    if poker_hands.one_pair(hand):
        return 1
    return hypergeometric_pmf(
        6,
        1,
        cards_remaining - 6,
        cards_to_draw - 1,
        cards_remaining,
        cards_to_draw
    )


def two_pair_probability(hand, cards_remaining, cards_to_draw):
    if poker_hands.one_pair(hand):
        probability = hypergeometric_pmf(
            4,
            2,
            cards_remaining - 4,
            cards_to_draw - 2,
            cards_remaining,
            cards_to_draw
        )
    else:
        probability = (
            nCr(3, 1)
            * hypergeometric_pmf(
                3,
                1,
                cards_remaining - 2 * 3,
                cards_to_draw - 2,
                cards_remaining,
                cards_to_draw
            )
        )
    return probability


def three_of_a_kind_probability(hand, cards_remaining, cards_to_draw):
    if poker_hands.one_pair(hand):
        probability = hypergeometric_pmf(
            2,
            1,
            cards_remaining - 2,
            cards_to_draw - 1,
            cards_remaining,
            cards_to_draw
        )
    else:
        probability = 2 * hypergeometric_pmf(
            3,
            2,
            cards_remaining - 2 * 3,
            cards_to_draw - 2,
            cards_remaining,
            cards_to_draw
        )
    return probability


def straight_probability(hand, cards_remaining, cards_to_draw):
    hand.sort(key=lambda card: cards.ranking(card))

    high_card = hand[1]
    low_card = hand[0]
    low_card_rank = cards.ranking(low_card)
    high_card_rank = cards.ranking(high_card)

    card_gap = cards.ranking(high_card) - cards.ranking(low_card)

    if card_gap > 4 and cards_to_draw < 4:
        return 0
    elif card_gap < 4 and cards_to_draw < 3:
        return 0

    if card_gap > 4:
        p_lower_straight = p_outside_straight(cards_remaining, cards_to_draw, low_card_rank)
        p_higher_straight = p_outside_straight(cards_remaining, cards_to_draw, high_card_rank)
        p_straight = p_lower_straight + p_higher_straight
    else:
        p_straight = 0

    return p_straight


def p_outside_straight(cards_remaining, cards_to_draw, low_card_rank):
    n_straights = min(5, min(low_card_rank, 12 - low_card_rank))
    return (
               (
                   n_straights
                   * math.pow(nCr(4, 1), 4)
                   * nCr(cards_remaining - 4 * 4, cards_to_draw - 4)
               )
               - n_straights
           ) / nCr(50, cards_to_draw)


# See: https://en.wikipedia.org/wiki/Hypergeometric_distribution
def hypergeometric_pmf(outs, outs_required, non_outs, non_outs_to_draw, cards_remaining, cards_to_draw):
    return (
        (nCr(outs, outs_required) * nCr(non_outs, non_outs_to_draw))
        / nCr(cards_remaining, cards_to_draw)
    )


def nCr(n, r):
    return sp.comb(n, r, exact=False)


def null_probability(hand, cards_remaining, turn):
    return 0
