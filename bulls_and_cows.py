'''
author = Michal Tomasek
'''

import random
from math import floor
from time import sleep, time

sepa = "░▒▓█▓▒" * 9 + "░"

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
    sleep(0.4)
print(sepa)
print(" WELCOME TO THE ULTIMATE GAME OF BULLS AND COWS!\n Four digit number is ready for you now!\n Remember, there are no duplicate digits in the number\n and the number can't start with zero.\n Now get to it, your time's running!")
print(sepa)

repeat = True         #This is a second (worse) option for the while loop below.
while repeat:
    number = random.choice(range(1000, 10000))
    for digit in str(number):
        if str(number).count(digit) > 1:
            repeat = True
    repeat = False

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
start = time()

while True:                                          #Main loop for the game
    guess = input("\n Enter a number: ")

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
        print(f" HOLY MOLLY! YOU DID IT! \n It took 'only' {attempts} attempts and {floor(total_time/60)} min and {floor(total_time%60)} sec.\n You have collected {total_bull} bulls and {total_cow} cows in total. That's quite a herd.")
        if input(f" Wanna go again? (y/n) ") != "y":
            print(" Thank you for playing! You still have a lot to learn though...")
            sleep(5)
            exit()
        else:
            print(sepa)
            number = num_generator()

    bull, cow = 0, 0



