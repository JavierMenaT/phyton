"""
File: Bucle While
Author: Javier Mena
Class: CSE 110
Number: 16
Date: October, 27 
"""

import random

magic_number = random.randint(1, 20)


guess = -1


while guess != magic_number:
    guess = int(input("What is your guess? "))

    if guess < magic_number:
        print("Higher")
    elif guess > magic_number:
        print("Lower")
    else:
        print("You guessed it!")