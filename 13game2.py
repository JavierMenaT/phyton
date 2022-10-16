"""
File: Game with If Statements
Author: Javier Mena
Class: CSE 110
Number: 13
Date: October, 14 
"""

name = input("Hi, are you ready to start?, first tell me your name or choose a nickname: ")
print(f"Hello! {name.upper()}, a world problem has broken out and you will have to fight to survive.")

weapon = input("What weapon would you use to defend yourself in a 'zombie apocalypse' a SWORD or a SHOTGUN?: ")

if weapon.lower() == "sword":
    print("Good choice, but you will have to wait until you are close to the zombies to kill them, you must be careful.")
    animal = input(f"The {weapon.upper()} it helps a lot but, an extra help wouldn't be bad, which animal would you like to help you: a HORSE or a DOG: ")
    if animal.lower() == "horse":
        print(f"Have you chosen a {animal.upper()}. You want to move fast, don't you? that will help you to escape if things get difficult.")
        print(f"Good {name.upper()} you have decided to fight with a {weapon.upper()} and a {animal.upper()} I'm sure you'll do well, see you next time")
    else:
        print(f"Have you chosen a {animal.upper()}. You want me to help you track and surprise the Zombies, very clever!")
        print(f"Good {name.upper()} you have decided to fight with a {weapon.upper()} and a {animal.upper()} I'm sure you'll do well, see you next time")        
if weapon.lower() == "shotgun":
    print("Not bad, with it you can kill them from a good distance, but have you ever wondered, What you would do if you ran out of ammunition? ")
    animal = input(f"The {weapon.upper()} it helps a lot but, an extra help wouldn't be bad, which animal would you like to help you: a HORSE or a DOG: ")
    if animal.lower() == "dog":
        print(f"Have you chosen a {animal.upper()}. You want me to help you track and surprise the Zombies, very clever!")
        print(f"Good {name.upper()} you have decided to fight with a {weapon.upper()} and a {animal.upper()} I'm sure you'll do well, see you next time")
    else:
        print(f"Have you chosen a {animal.upper()}. You want to move fast, don't you? that will help you to escape if things get difficult.")
        print(f"Good {name.upper()} you have decided to fight with a {weapon.upper()} and a {animal.upper()} I'm sure you'll do well, see you next time")