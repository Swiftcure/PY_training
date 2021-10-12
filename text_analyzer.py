'''
author = Michal Tomasek
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

from time import sleep                  #Added for smooth exits.
sepa = "#" * 70
users_all = {"bob": "123", "ann": "pass123", "mike": "password13", "liz": "pass123"}
user = input("Username: ").lower()      #lower() is not neccessary, name is usual case sensitive, but better be safe than sorry
if user not in users_all:
    print("Invalid user. Exiting in 5 seconds.")
    sleep(5)
    exit()
password = input("Password: ")
if password != users_all[user]:
    password_2 = input("""Incorrect password.
There are no mistakes, just happy accidents.
You can try one more time: """)
    if password_2 != users_all[user]:
        print("Try writing down your password next time. Exiting in 5 seconds.")
        sleep(5)
        exit()
    else:
        print(sepa)
        print(f"You remembered, noice! Welcome, {user.title()}!")
else:
    print(sepa)
    print(f"Welcome, {user.title()}!")

print("There are valuable ancient texts for you to analyze!")
choice = input("Choose wisely your number from 1 to 3: ")

if choice.isnumeric() != True:
    print("Number... jeeeez... Exiting in 5 seconds.")
    sleep(5)
    exit()
elif int(choice) not in range(1,4):
    print("From 1 to 3. It wasn't that hard, was it? Exiting in 5 seconds.")
    sleep(5)
    exit()
else:
    print("You have chosen", end="")                   #Uncomment for extra suspense!
    for i in range(6): print('.', end=""), sleep(1)
    print("WISELY!")
    print("Let's get to it!")
print(sepa)

chosen_text = TEXTS[int(choice) - 1]
words_only = chosen_text.split()

text_clean = [ w.strip(".,") for w in words_only ]

words_total = int()                         #Number of words in total
for w in text_clean: words_total += 1
print(f"There are {words_total} words in the selected text.")

words_title = int()                         #Number of titlecase words
for w in text_clean:
    if w[0].isupper() and w[1:].lower():
        words_title += 1
print(f"There are {words_title} titlecase words.")

words_upper = int()                         #Number of uppercase words
for w in text_clean:                        #Question is, how to deal with words like "30N". It's an uppercase word imho, so I'm gonna treat it that way.
    if w.isupper():                         #Possible solution would also be adding "and w.isalpha()".
        words_upper += 1
print(f"There are {words_upper} uppercase words.")

words_lower = int()                         #Number of lowercase words
for w in text_clean:
    if w.islower():
        words_lower += 1
print(f"There are {words_lower} lowercase words.")

num_strings = int()                         #Number of numeric strings
for w in text_clean:
    if w.isnumeric():
        num_strings += 1
print(f"There are {num_strings} numeric strings.")

num_sum = int()                             #The total sum of numbers
for w in text_clean:
    if w.isnumeric():
        w = int(w)
        num_sum += w
print(f"The sum of all the numbers is {num_sum}.")

print(sepa)   

len_dict = {}
for w in text_clean: len_dict[len(w)] = len_dict.get(len(w), 0) + 1

mid_col_space = max(len_dict.values()) + 2
print(f"LEN|{'OCCURENCES'.center(mid_col_space)}|NR.")
print(sepa)
for n in len_dict:
    print(f"{n:>3}|{('*' * len_dict[n]):<{mid_col_space}}|{len_dict[n]:<3}")
print(sepa)
input("Well, this was fun! Until next time! Type anything to end: \n")





