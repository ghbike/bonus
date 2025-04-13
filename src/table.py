from hand import Hand
from deck import Deck
from time import time
import random


class Table:
    cnt_dct = {"Diamond Royal Flush": 0, "Royal Flush": 0,
           "Straight Flush": 0, "4oak": 0, "Full house": 0,
           "Flush": 0, "Straight": 0, "3oak": 0, "No game": 0}
    table_float = 0
    jp_start = 50_000
    increment = .015
    min_bet = 5
    max_bet = 25
    bets = (5, 5, 5, 5, 10, 10, 10, 15, 20, 25)

    def __init__(self):
        self.deck = Deck()
        self.payout_table = {"Diamond Royal Flush": 0, "Royal Flush": 350,
            "Straight Flush": 200, "4oak": 300, "Full house": 100,
            "Flush": 75, "Straight": 50, "3oak": 10, "No game": 0}
        self. jp_payouts = {"Diamond Royal Flush": 1.00, "Royal Flush": .25,
            "Straight Flush": .20, "4oak": 0, "Full house": 0,
            "Flush": 0, "Straight": 0, "3oak": 0, "No game": 0}
        self.increment_table = {"Diamond Royal Flush": 0, "Royal Flush": 0,
            "Straight Flush": 0, "4oak": 0, "Full house": 0,
            "Flush": 0, "Straight": 0, "3oak": 0, "No game": self.increment}

    def one_hand_dealing(self):
        hand = Hand(self.deck)
        hand_game = hand.hand_is()
        bet = random.choice(self.bets)
        self.cnt_dct[hand_game] += 1


if __name__ == '__main__':
    time_start = time()

    table = Table()
    for i in range(2_5989_600):
        table.one_hand_dealing()

    time_end = time()
    total_time = time_end - time_start
    print(total_time)
    print(table.cnt_dct)
