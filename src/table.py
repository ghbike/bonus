from hand import Hand
from deck import Deck
from time import time
import random


class Table:
    cnt_dct = {"Diamond Royal Flush": 0, "Royal Flush": 0,
           "Straight Flush": 0, "4oak": 0, "Full house": 0,
           "Flush": 0, "Straight": 0, "3oak": 0, "No game": 0}
    table_float = 0
    jp = 50_000
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
        self.jp_payouts = {"Diamond Royal Flush": 1.00, "Royal Flush": .25,
            "Straight Flush": .20, "4oak": 0, "Full house": 0,
            "Flush": 0, "Straight": 0, "3oak": 0, "No game": 0}
        self.increment_table = {"Diamond Royal Flush": 0, "Royal Flush": 0,
            "Straight Flush": 0, "4oak": 0, "Full house": 0,
            "Flush": 0, "Straight": 0, "3oak": 0, "No game": self.increment}
        self.profit_table = {"Diamond Royal Flush": 0, "Royal Flush": 0,
                                "Straight Flush": 0, "4oak": 0, "Full house": 0,
                                "Flush": 0, "Straight": 0, "3oak": 0, "No game": 1}

    def __str__(self):
        return f"float: {self.table_float}, JP: {self.jp}"

    def one_hand_dealing(self):
        hand = Hand(self.deck)
        hand_game = hand.hand_is()
        bet = random.choice(self.bets)
        self.cnt_dct[hand_game] += 1

        self.table_float += self.profit_table[hand_game] * bet  # to float
        self.table_float -= self.payout_table[hand_game] * bet  # from float
        self.jp += self.increment_table[hand_game] * bet        # to jp
        self.jp -= round(self.jp * self.jp_payouts[hand_game] * bet/self.max_bet, 0) # from jp
        if self.jp < self.jp_start:  #increasing jp upto jp_start using float
            self.table_float += round(self.jp - self.jp_start, 0)
            self.jp = self.jp_start


if __name__ == '__main__':


    table = Table()
    for _ in range(10):
        time_start = time()
        for i in range(2_598_960):
            table.one_hand_dealing()

        time_end = time()
        total_time = time_end - time_start
        print(f'time: {round(total_time, 0)}')
        print(table.cnt_dct)
        print(table)
        print("-----------------------------")
