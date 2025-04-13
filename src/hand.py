from deck import Deck


class Hand:
    number = [0]

    def __init__(self, deck_):
        deck_.shuffling()
        self.cards = deck_.dealing()
        self.ranks_dct = {"A":0, "K":0, "Q":0, "J":0, "10":0, "9":0,
                          "8":0, "7":0, "6":0, "5":0, "4":0, "3":0, "2":0}
        for card in self.cards:
            self.ranks_dct[card.rank] += 1
        self.sorted_cards = sorted(self.ranks_dct.items(), key=lambda item: item[1], reverse=True)
        self.suits_set = set(card.suit for card in self.cards)
        self.ranks_lst = [card.rank for card in self.cards]
        self.ranks_set = set(self.ranks_lst)
        self.card_number = 5
        self.number[0] += 1

    def __str__(self):
        cards = "\n".join(card.__str__() for card in self.cards)
        return f"Hand {self.number[0]}:\n{cards}\n{self.hand_is()}\n-------------------"

    def is_straight(self):
        if self.ranks_set == {"A", "2", "3", "4", "5"}: return True
        if self.ranks_set == {"2", "3", "4", "5", "6"}: return True
        if self.ranks_set == {"3", "4", "5", "6", "7"}: return True
        if self.ranks_set == {"4", "5", "6", "7", "8"}: return True
        if self.ranks_set == {"5", "6", "7", "8", "9"}: return True
        if self.ranks_set == {"6", "7", "8", "9", "10"}: return True
        if self.ranks_set == {"7", "8", "9", "10", "J"}: return True
        if self.ranks_set == {"8", "9", "10", "J", "Q"}: return True
        if self.ranks_set == {"9", "10", "J", "Q", "K"}: return True
        return  self.is_royal()

    def is_flush(self):
        return len(self.suits_set) == 1

    def is_royal(self):
        return  self.ranks_set == {"10", "J", "Q", "K", "A"}

    def is_diamonds(self):
        return self.suits_set == {'Diamonds'}

    def hand_is(self):
        match self.sorted_cards[0][1]:
            case 5:
                return "MISTAKE"
            case 4:
                return "4oak"
            case 3:
                if self.sorted_cards[1][1] == 2:
                    return "Full house"
                else:
                    return "3oak"
            case 2:
                if self.sorted_cards[1][1] == 2:
                    return "2 Pairs"
                else:
                    return "Pair"
            case 1:
                if not self.is_straight():
                    if not self.is_flush():
                        return "No game"
                    else:
                        return "Flush"
                elif not self.is_flush():
                    return "Straight"
                else:
                    if not self.is_royal():
                        return "Straight Flush"
                    elif self.is_diamonds():
                        return "Diamond Royal Flush"
                    else:
                        return "Royal Flush"
