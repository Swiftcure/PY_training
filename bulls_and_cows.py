'''
author = Michal Tomasek
'''

import getpass
import random
from time import sleep

sepa = "░▒▓█▓▒" * 9 + "░"

#print(sepa)
#logo = """
#
#██████╗ ██╗   ██╗██╗     ██╗     ███████╗
#██╔══██╗██║   ██║██║     ██║     ██╔════╝
#██████╔╝██║   ██║██║     ██║     ███████╗
#██╔══██╗██║   ██║██║     ██║     ╚════██║
#██████╔╝╚██████╔╝███████╗███████╗███████║
#╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝
#
# █████╗ ███╗   ██╗██████╗
#██╔══██╗████╗  ██║██╔══██╗
#███████║██╔██╗ ██║██║  ██║
#██╔══██║██║╚██╗██║██║  ██║
#██║  ██║██║ ╚████║██████╔╝
#╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝
#
# ██████╗ ██████╗ ██╗    ██╗███████╗
#██╔════╝██╔═══██╗██║    ██║██╔════╝
#██║     ██║   ██║██║ █╗ ██║███████╗
#██║     ██║   ██║██║███╗██║╚════██║
#╚██████╗╚██████╔╝╚███╔███╔╝███████║
# ╚═════╝ ╚═════╝  ╚══╝╚══╝ ╚══════╝
#"""
#
#for line in logo.split("\n"):
#    print(line)
#    sleep(0.5)
#print(sepa)
#print("WELCOME TO THE ULTIMATE GAME OF BULLS AND COWS!\nFour digit number is ready for you now!\nRemember, there are no duplicate digits in the number\nand the number can't start with zero.")
#print(sepa)

#repeat = True                                      # This is just another dumber version of the while loop below (for educational purposes).
#while repeat:
#    repeat = False
#    number = random.choice(range(1000, 10000))
#    for digit in str(number):
#       if str(number).count(digit) > 1:
#           repeat = True
#           break

while True:
    number = str(random.choice(range(1000, 10000)))
    if len(set(number)) == 4
        break

print(number)

while True:
    guess = input("Enter a number: ")
    if guess.isnumeric() and len(guess) == 4 and guess[0] != "0" and len(set(guess)) == 4:
        break
    else:
        print("Four... digit-unique... number... not starting with zero. It's not so difficult.")

print(guess)



