'''
author = Michal Tomasek
'''

import numpy
from time import sleep

LETTER_LIST = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T"]

X_ROW = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7,
         'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14,
         'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19}

Y_ROW = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

PF_CELL_TOP = "┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐"
PF_CELL_MID = "├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤"
PF_CELL_BOT = "└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘"
PF_CELL_SIDE = "│"

playfield = numpy.full((20, 20), "0", dtype=str)

def show_playfield():
    for letter in X_ROW.keys():
        print(f"{' ' * 4}{letter}", end="") if letter == "A" else print(f"{' ' * 3}{letter}", end="")

    for i_row, row in enumerate(playfield):
        print("\n  " + PF_CELL_TOP) if i_row == 0 else None

        for i_value, value in enumerate(row):
            if i_value == 0:
                print(f" {Y_ROW[i_row]+1}", end="") if Y_ROW[i_row] < 9 else print(f"{Y_ROW[i_row]+1}", end="")
            print(f"{PF_CELL_SIDE} {' ' if value == '0' else value} ", end="")

        print(PF_CELL_SIDE, end="")
        print("\n  " + PF_CELL_BOT) if i_row == 19 else print("\n  " + PF_CELL_MID)

def game_mode():
    while True:
        game_mode_choice = input("Choose between game for 2 player (2P) or versus computer (PC): ")
        if game_mode_choice in ["2P", "PC"]:
            break

#show_playfield()

def mode_2p():
    while True:
        p_o = input("Player O enter your coordinates: ")
        print(p_o[0])
        print(p_o[0].isalpha())
        print(p_o[1:])
        print(p_o[1:].isnumeric())
        print(len(p_o))
        print(p_o[1:] in Y_ROW)
        print(p_o[0] in X_ROW.keys())
        while p_o[0].isalpha() == False or p_o[1:].isnumeric() == False or len(p_o) > 3 or int(p_o[1:]) not in Y_ROW or p_o[0] not in X_ROW.keys():
            p_o = input("Player 'O', please, enter proper coordinates: ")
#        playfiled[][] = 'O'

#mode_2p()
#p_o = input("Player 'O' enter you coordinates: ")
#print(X_ROW[p_o[0]])