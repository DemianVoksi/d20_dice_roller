#!/usr/bin/env python

# import
from random import randint

# functions
def dy(y): 
    return randint(1, y) 

def xdy(x, y): 
    return list(dy(y) for i in range(x))

def roll():
    while True: 
        print("Please enter the number of sides you want your die to have. You can choose between:", dice)
        y = int(input("Which die do you want to roll? "))
        x = int(input("How many dice do you want to roll? You can choose any number: "))
        if y in dice:
            rolldice = list(xdy(x, y))
            print(rolldice)
            print("The sum of your roll is", (sum(rolldice)))
            break
        else:
            print("Please choose the correct type of die.")

# dice
dice = [4, 6, 8, 10, 12, 20, 100]

# roll
roll()

#roll again
while True:
    roll_again = int(input("Do you want to roll again? Press (1) to roll again and (2) to exit: "))
    if roll_again == 1:
        roll()
    elif roll_again == 2:
        break
    else:
        pass



