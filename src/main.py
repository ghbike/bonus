from time import time
from hand import Hand
from deck import Deck


def cards_dealing(cycle=1):
    dct = {"Diamond Royal Flush": 0, "Royal Flush": 0, "Straight Flush": 0,
           "4oak": 0, "Full house": 0, "Flush": 0, "Straight": 0, "3oak": 0,
           "2 Pairs": 0, "Pair": 0, "No game": 0, "MISTAKE": 0}
    deck = Deck()
    for _ in range(cycle):
        hand = Hand(deck)
        dct[hand.hand_is()] += 1

    return dct


if __name__ == '__main__':

    time_start = time()
    results = cards_dealing(25_989_600)
    time_end = time()
    total_time = time_end - time_start
    print(f'время работы: {round(total_time, 2)}')
    print(f'Diamonds: {results["Diamond Royal Flush"]}')
    print(f'Royal Flush: {results["Royal Flush"]}')
    print(f'Straight Flush: {results["Straight Flush"]}')
    print(f'4oak: {results["4oak"]}')
    print(f'Full house: {results["Full house"]}')
    print(f'Flush: {results["Flush"]}')
    print(f'Straight: {results["Straight"]}')
    print(f'3oak: {results["3oak"]}')
    print(f'2 Pairs: {results["2 Pairs"]}')
    print(f'Pair: {results["Pair"]}')
    print(f'No game: {results["No game"]}')
    print(f'MISTAKE: {results["MISTAKE"]}')
