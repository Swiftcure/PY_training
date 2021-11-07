'''
author = Michal Tomasek
'''

import numpy

letter_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T"]

x_row = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7,
         'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14,
         'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19}

y_row = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

y_row_2 = []
for n in y_row: y_row_2.append(str(n+1).zfill(2))

print(y_row_2)


pf_cell_top = "┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐"
pf_cell_mid = "├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤"
pf_cell_bot = "└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘"
pf_cell_side = "│"

playfield = numpy.full((20, 20), "0", dtype=str)
print(type(playfield))
playfield[7][11] = "X"

for letter in x_row.keys():
    print(f"{' ' * 4}{letter}", end="") if letter == "A" else print(f"{' ' * 3}{letter}", end="")

#print("\n" + pf_cell_top + "\n", end="")
for i_row, row in enumerate(playfield):
    print("\n  " + pf_cell_top) if i_row == 0 else None

    for i_value, value in enumerate(row):
        if i_value == 0:
            print(f" {y_row[i_row]+1}", end="") if y_row_2[i_row] < "10" else print(f"{y_row[i_row]+1}", end="")
        print(f"{pf_cell_side} {' ' if value == '0' else value} ", end="")

    print(pf_cell_side, end="")
    print("\n  " + pf_cell_bot) if i_row == 19 else print("\n  " + pf_cell_mid)


