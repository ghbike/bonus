from table import Table
from time import time


bets = 0
time_start = time()
table = Table()

for session in range(10):
    print(session)
    for hand in range(259_896_000):
        table.one_hand_dealing()

    time_end = time()
    total_time = time_end - time_start
    print(f'\ntime: {round(total_time)}       bets: {table.bets_total}')
    print(table.cnt_dct)
    print(table, round(100 * table.table_float / table.bets_total, 2))
    print(f"max JP: {round(max(table.jp_lst))}")
    print(f"sum p/o: {sum(table.table_payouts_lst)}")
    print(f"sum JP p/o: {sum(table.jp_payouts_lst)}")
    print(f"max JP p/o: {max(table.jp_payouts_lst)}")
    print(f"sum magic p/o: {sum(table.magic_payouts_lst)}")
    print(f"sum mistery p/o: {sum(table.mistery_payouts_lst)}")
    print(f"sum increments: {round(sum(table.increment_lst))}")
    print(f"sum auto refill: {round(sum(table.auto_refill_lst))}")
    print("-----------------------------")


