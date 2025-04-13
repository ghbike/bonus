from card import Card
import random


class Deck:
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits = ["Hearts", "Spades", "Clubs", "Diamonds"]

    def __init__(self, deck_number=1):
        self.deck_number = deck_number
        self.cards = []
        for _ in range(self.deck_number):
            for suit in Deck.suits:
                for rank in Deck.ranks:
                    self.cards.append(Card(rank, suit))
        self.card_number = len(self.cards)

    def shuffling(self):
        random.shuffle(self.cards)

    def dealing(self):
        return self.cards[:5]
