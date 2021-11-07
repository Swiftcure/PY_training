'''
author = Michal Tomasek
'''

import random
from math import floor
from time import sleep, time

sepa = "░▒▓█▓▒" * 10 + "░" + "\n"

print(sepa)
logo = """
 ██████╗ ██╗   ██╗██╗     ██╗     ███████╗
 ██╔══██╗██║   ██║██║     ██║     ██╔════╝
 ██████╔╝██║   ██║██║     ██║     ███████╗
 ██╔══██╗██║   ██║██║     ██║     ╚════██║
 ██████╔╝╚██████╔╝███████╗███████╗███████║
 ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝

  █████╗ ███╗   ██╗██████╗
 ██╔══██╗████╗  ██║██╔══██╗
 ███████║██╔██╗ ██║██║  ██║
 ██╔══██║██║╚██╗██║██║  ██║
 ██║  ██║██║ ╚████║██████╔╝
 ╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝

  ██████╗ ██████╗ ██╗    ██╗███████╗
 ██╔════╝██╔═══██╗██║    ██║██╔════╝
 ██║     ██║   ██║██║ █╗ ██║███████╗
 ██║     ██║   ██║██║███╗██║╚════██║
 ╚██████╗╚██████╔╝╚███╔███╔╝███████║
  ╚═════╝ ╚═════╝  ╚══╝╚══╝ ╚══════╝
  """

for line in logo.split("\n"):
    print(line)
    sleep(0.3)
print(sepa)

intro =""" WELCOME TO THE ULTIMATE GAME OF BULLS AND COWS!
 You will be given a four digit number to guess.
 There are no duplicate digits in the number
 and the number can't start with zero.
 For every guess that the you make,
 you get 2 values - the number of bulls
 and the number of cows. 1 bull means
 the guess contains and the target number have
 1 digit in common, and in the correct position.
 1 cow means the guess and the target have
 1 digit in common, but not in correct position.
 Let the target be 1234. Guessing 4321 will give
 0 bulls and 4 cows. 3241 will give 1 bull and 3 cows.
 4 bulls means you have won the game!

"""

for char in intro:
    print(char, flush=True, end="")
    sleep(0.05)

print(sepa)

def num_valid_check(guess):
    while True:
        if guess.isnumeric() and guess[0] != "0" and len(set(guess)) == 4:
            return 1
        else:
            print(" Four... digit-unique... number... not starting with zero. It's not so difficult.")
            return 0

def num_generator():
    while True:
        number = str(random.choice(range(1000, 10000)))
        if len(set(number)) == 4:
            return number

number = num_generator()
bull, cow = 0, 0
total_bull, total_cow = 0, 0
attempts = 0
input(" Your number is ready for you now! Are you ready? (y/n) ")
print(" No one cares, if you are ready or not...\n Here we go! Time's running, get to it!\n")
sleep(3)
start = time()

while True:                                          #Main loop for the game
    guess = input(" Enter a number: ")

    if num_valid_check(guess) == False:
        continue

    for n in guess:
        if n == number[guess.index(n)]:
            bull += 1
        elif n != number[guess.index(n)] and n in number:
            cow += 1

    print(f" BULLS: {bull}\n COWS: {cow}")

    attempts += 1
    total_bull += bull
    total_cow += cow

    if bull == 4:
        end = time()
        total_time = end - start
        print(f" HOLY MOLLY! YOU DID IT! \n It took 'only' {attempts} {'attempt' if attempts == 1 else 'attempts'} "
              f"and {floor(total_time/60)} min and {floor(total_time%60)} sec.\n "
              f"You have collected {total_bull} bulls and {total_cow} cows in total."
              f"\n That's quite a herd. Keep then coming!")
        if input(f" Wanna go again? (y/n) ") != "y":
            print(" Thank you for playing! You still have a lot to learn though...")
            sleep(5)
            exit()
        else:
            print("\n" + sepa)
            number = num_generator()
            attempts = 0
            start = time()

    bull, cow = 0, 0



