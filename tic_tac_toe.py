'''
author = Michal Tomasek
'''

import numpy
from time import sleep

LETTER_LIST = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T"]

#X_ROW = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7,
#         'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14,
#         'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19}
X_ROW = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8,
         'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
         'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20}
Y_ROW = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

PF_CELL_TOP = "┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐"
PF_CELL_MID = "├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤"
PF_CELL_BOT = "└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘"
PF_CELL_SIDE = "│"

playfield = numpy.full((20, 20), 0, dtype=str)

def show_playfield():
    for letter in X_ROW.keys():
        print(f"{' ' * 4}{letter}", end="") if letter == "A" else print(f"{' ' * 3}{letter}", end="")

    for i_row, row in enumerate(playfield):
        print("\n  " + PF_CELL_TOP) if i_row == 0 else None

        for i_value, value in enumerate(row):
            if i_value == 0:
                print(f" {Y_ROW[i_row]}", end="") if Y_ROW[i_row] <= 9 else print(f"{Y_ROW[i_row]}", end="")
            print(f"{PF_CELL_SIDE} {' ' if value == '0' else value} ", end="")

        print(PF_CELL_SIDE, end="")
        print("\n  " + PF_CELL_BOT) if i_row == 19 else print("\n  " + PF_CELL_MID)

def choose_game_mode() -> str:
    while True:
        game_mode_choice = input("Choose between game for 2 player (2P) or versus computer (PC): ")
        if game_mode_choice in ["2P", "PC"]:
            break
    return game_mode_choice

#show_playfield()

def field_check(in_vals) -> (list, list):
    surroundings = [[in_vals[1] - 1, in_vals[0] - 1], [in_vals[1] - 1, in_vals[0]], [in_vals[1] - 1, in_vals[0] + 1],
                    [in_vals[1], in_vals[0] - 1], [in_vals[1], in_vals[0] + 1],
                    [in_vals[1] + 1, in_vals[0] - 1], [in_vals[1] + 1, in_vals[0]], [in_vals[1] + 1, in_vals[0] + 1]]
    cross_positions = []
    circle_positions = []
    for pos in surroundings:
        print(pos)
        print(playfield[pos[1]][pos[0]])
        if pos[0] not in X_ROW.values() or pos[1] not in Y_ROW:
            continue
        if playfield[pos[1]][pos[0]] == 0:
            continue
        elif playfield[pos[1]][pos[0]] == "X":
            cross_positions.append(pos)
        else:
            circle_positions.append(pos)
    print(cross_positions)
    print(circle_positions)
    return (cross_positions, circle_positions)

def check_direction(pos1:list, pos2:list):
    x_dir = pos2[0] - pos1[0]
    y_dir = pos2[1] - pos1[0]
    count = 2
    if playfield[pos2[1] + y_dir][pos2[0] + x_dir] == "X":
        count += 1


def overall_check():
    for y in Y_ROW:
        for x in X_ROW.values():
            if playfield[y][x] == "X":
                fc1_cro_pos, fc1_cir_pos = field_check([x, y])         #field check 1 cross postions
                for pos in fc1_cro_pos:
                    if playfield[pos[0]][pos[1]] == "X":
                        check_direction([x, y], [pos[0], pos[1]])



                    fc_x_cro_pos, fc_x_cir_pos = field_check()

def mode_2p():
    available_players = ["X", "O"]
    player = "X"
    turns = 0
    while True:
        player_input = input(f"Player {player} enter your coordinates: ").upper()
        input_values = [X_ROW[player_input[0]], int(player_input[1:])]
        print(f"input_values {input_values}")
        if player_input[0].isalpha() == False or player_input[1:].isnumeric() == False or len(player_input) > 3 or int(player_input[1:]) not in Y_ROW or player_input[0] not in X_ROW.keys():
            player_input_fix = player_input
            while player_input_fix[0].isalpha() == False or player_input_fix[1:].isnumeric() == False or len(player_input_fix) > 3 or int(player_input_fix[1:]) not in Y_ROW or player_input_fix[0] not in X_ROW.keys():
                player_input_fix = input(f"Player {player}, please, enter proper coordinates: ")
            input_values = [X_ROW[player_input_fix[0]], int(player_input_fix[1:])]


        field_check(input_values)
        playfield[input_values[1] - 1][input_values[0] - 1] = player
        show_playfield()
        turns += 1
        player = available_players[turns % 2]

playfield[1][1] = "X"
mode_2p()

