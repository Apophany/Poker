import deck as dk
import poker_hands as ph


def generate_initial_state(num_players):
    initial_deck = dk.Deck()
    return deal(initial_deck, num_players)


def deal(deck, num_players):
    player_hands = [None] * num_players
    for i in xrange(num_players * 2):
        current_hand = player_hands[(i / 2) - 1]

        if current_hand:
            current_hand.append(deck.pop())
        else:
            current_hand = [deck.pop()]
            player_hands[(i / 2) - 1] = current_hand

    for hand in player_hands:
        print hand
        print (ph.high_card(hand))


if __name__ == "__main__":
    generate_initial_state(5)
