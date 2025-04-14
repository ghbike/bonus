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
    bets = (5, 5, 5, 5, 5, 5, 10, 15, 20, 25)  # average = 10
    bets_total = 0

    def __init__(self):
        self.deck = Deck()
        self.payouts = {"Diamond Royal Flush": 0, "Royal Flush": 350,
            "Straight Flush": 200, "4oak": 300, "Full house": 100,
            "Flush": 75, "Straight": 50, "3oak": 10, "No game": 0}
        self.jp_payouts = {"Diamond Royal Flush": 1.00, "Royal Flush": .25,
            "Straight Flush": .20, "4oak": 0, "Full house": 0,
            "Flush": 0, "Straight": 0, "3oak": 0, "No game": 0}
        self.magic = {"Magic Card": (1 / 50, 8), "Mistery p/o": (1 / 1_000, 10)}

    def __str__(self):
        return f"float: {self.table_float}, JP: {round(self.jp, 2)}"

    def one_hand_dealing(self):
        # ------------------------------- Dealing ---------------------------------
        bet = random.choice(self.bets)
        self.bets_total += bet
        hand = Hand(self.deck)
        hand_game = hand.hand_is()
        self.cnt_dct[hand_game] += 1
        # ------------------------------- Magic -----------------------------------
        magic_payment = 0
        mistery_payment = 0
        if random.random() < self.magic["Magic Card"][0]:
            magic_card = random.choice(self.deck.cards)
            if magic_card in hand.cards:
                magic_payment = self.magic["Magic Card"][1]
        if random.random() < self.magic["Mistery p/o"][0]:
            mistery_payment = self.magic["Mistery p/o"][1]
        # --------------------------------payouts-----------------------------------
        payout = self.payouts[hand_game] * bet
        magic_payout = (magic_payment + mistery_payment) * bet
        jp_payout = round(self.jp_payouts[hand_game] * self.jp, 0)
        if not (payout + magic_payout + jp_payout):      # if bonus bet loses
            float_profit = bet
            jp_profit = bet * self.increment
            self.table_float += float_profit
            self.jp += jp_profit
        else:                                            # if bonus bet wins
            self.table_float -= payout + magic_payout + jp_payout
            self.jp -= jp_payout
        if self.jp < self.jp_start: self.jp = self.jp_start    # jp auto refill
        return bet

if __name__ == '__main__':


    bets = 0
    table = Table()
    for _ in range(5):
        time_start = time()
        for i in range(25_989_600):
            table.one_hand_dealing()
        time_end = time()
        total_time = time_end - time_start
        print(f'time: {round(total_time, 0)}  #: {_}  bets: {table.bets_total}')
        print(table.cnt_dct)
        print(table, 100 * table.table_float / table.bets_total)
        print("-----------------------------")
