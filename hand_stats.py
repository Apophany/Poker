import poker_hands
import scipy.special as sp


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
        poker_hands.THREE_OF_A_KIND: three_of_a_kind_probability
    }.get(hand_rank, null_probability)(hand, cards_remaining, cards_to_draw)


def one_pair_probability(hand, cards_remaining, cards_to_draw):
    if poker_hands.one_pair(hand):
        return 1
    return hypergeometric_pmf(6, 1, cards_remaining - 6, cards_to_draw - 1, cards_remaining, cards_to_draw)


def three_of_a_kind_probability(hand, cards_remaining, cards_to_draw):
    if poker_hands.one_pair(hand):
        probability = hypergeometric_pmf(2, 1, cards_remaining - 2, cards_to_draw - 1, cards_remaining, cards_to_draw)
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


# See: https://en.wikipedia.org/wiki/Hypergeometric_distribution
def hypergeometric_pmf(outs, outs_required, non_outs, non_outs_to_draw, cards_remaining, cards_to_draw):
    return (
        (
            sp.comb(outs, outs_required)
            * sp.comb(non_outs, non_outs_to_draw)
        )
        / sp.comb(cards_remaining, cards_to_draw)
    )


def null_probability(hand, cards_remaining, turn):
    return 0
