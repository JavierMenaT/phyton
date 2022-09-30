from ast import Str
"""
File: Numeric Data Types
Author: Javier Mena
Class: CSE 110
Number: 6
"""

age=input("How old are you? ")
print("On your next birthday, you will be", int(age)+1,)

print()

eggs=input("How many eggs cartons do you have? ")
print("You have ",int(eggs)*12, "eggs")

print()

cookies=input("How many cookies do you have? ")
people=input("How many people are there? ")
print("Each person may have ",int(cookies)/int(people))