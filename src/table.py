from hand import Hand
from deck import Deck
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
        self.bet_lst = [0]
        self.hand_lst = [None]
        self.magic_payouts_lst = [0]
        self.mistery_payouts_lst = [0]
        self.table_payouts_lst = [0]
        self.jp_payouts_lst = [0]
        self.float_lst = [0]
        self.jp_lst = [self.jp_start]
        self.increment_lst = [0]
        self.auto_refill_lst = [0]

    def __str__(self):
        return f"float: {self.table_float}, JP: {round(self.jp, 2)}"

    def one_hand_dealing(self):
        # ------------------------------- Dealing ---------------------------------
        bet = random.choice(self.bets)
        self.bet_lst.append(bet)
        self.bets_total += bet
        hand = Hand(self.deck)
        hand_game = hand.hand_is()
        self.cnt_dct[hand_game] += 1
        self.hand_lst.append(hand_game)
        # ------------------------------- Magic -----------------------------------
        magic_payment = 0
        mistery_payment = 0
        if random.random() < self.magic["Magic Card"][0]:
            magic_card = random.choice(self.deck.cards)
            if magic_card in hand.cards:
                magic_payment = self.magic["Magic Card"][1] * bet
        if random.random() < self.magic["Mistery p/o"][0]:
            mistery_payment = self.magic["Mistery p/o"][1] * bet
        # --------------------------------payouts-----------------------------------
        self.magic_payouts_lst.append(magic_payment)
        self.mistery_payouts_lst.append(mistery_payment)
        payout = self.payouts[hand_game] * bet
        magic_payout = magic_payment + mistery_payment
        jp_payout = round(self.jp_payouts[hand_game] * self.jp, 0)
        self.table_payouts_lst.append(payout)
        self.jp_payouts_lst.append(jp_payout)

        jp_profit = 0                                    # if bonus bet loses
        if not (payout + magic_payout + jp_payout):
            float_profit = bet
            jp_profit = bet * self.increment
            self.table_float += float_profit
            self.jp += jp_profit
        else:                                            # if bonus bet wins
            self.table_float -= payout + magic_payout + jp_payout
            self.jp -= jp_payout

        jp_refill = 0                                    # jp auto refill
        if self.jp < self.jp_start:
            jp_refill = self.jp_start - self.jp
            self.jp = self.jp_start
        self.auto_refill_lst.append(jp_refill)

        self.float_lst.append(self.table_float)
        self.jp_lst.append(self.jp)
        self.increment_lst.append(jp_profit)
