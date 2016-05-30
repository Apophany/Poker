import cards
import random as rnd


class Deck:
    def __init__(self):
        self.cards = []
        for suit in cards.suits():
            for rank in cards.ranks():
                self.cards.append({
                    'suit': suit,
                    'rank': rank
                })
        rnd.shuffle(self.cards)

    def shuffle(self):
        rnd.shuffle(self.cards)
        return self.cards

    def pop(self):
        return self.cards.pop()

    def remaining_cards(self):
        return len(self.cards)
