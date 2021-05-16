from random import randint
import math

tests = 1000

list = []
coin = ["H","T"]
bob_flips = sally_flips = 0

for test in range(0,tests + 1):
    list = []
    bob_won = sally_won = False
    for flip in range(0,100):
        coinflip = coin[randint(0,1)]
        list.append(coinflip)
        if len(list) >= 2:
            if list[(len(list))- 2] == "H" and list[(len(list)) - 1] == "T" and not sally_won:
                sally_won = True
                sally_flips += len(list)
            if list[(len(list))- 2] == "H" and list[(len(list)) - 1] == "H" and not bob_won:
                bob_won = True
                bob_flips += len(list)
            if bob_won and sally_won:
                break
    if test == tests:
        print("\nIn " + str(tests) + " coin flips, ")
        print("Sally average number of flips to win: " + str((round((sally_flips / tests),2))))
        print("Bob average number of flips to win: " + str((round((bob_flips / tests),2))))
        print("\nBob took " + str(round(((bob_flips - sally_flips)/tests),2)) + " more flips to win, on average.")
