import poker_hands
import scipy.special as sp


def hand_probabilities(hand, cards_remaining, cards_to_draw, table_cards=None):
    probabilities = {}
    for hand_rank in poker_hands.hand_ranks():
        probabilities[hand_rank] = calculate_prob(hand_rank, hand, cards_remaining, cards_to_draw)
    return probabilities


def calculate_prob(hand_rank, hand, cards_remaining, cards_to_draw):
    return {
        poker_hands.ONE_PAIR: one_pair_probability
    }.get(hand_rank, null_probability)(hand, cards_remaining, cards_to_draw)


# Uses hypergeometric PMF
def one_pair_probability(hand, cards_remaining, cards_to_draw):
    if poker_hands.one_pair(hand):
        return 1

    probability = (
        (sp.comb(6, 1) * sp.comb(cards_remaining - 6, cards_to_draw - 1))
        / sp.comb(cards_remaining, cards_to_draw)
    )
    return probability


def null_probability(hand, cards_remaining, turn):
    return 0
