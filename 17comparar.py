"""
File: Bucle While
Author: Javier Mena
Class: CSE 110
Number: 17
Date: October, 30 
"""
palabra_secreta = "mormon"
guess = ""
numero_intentos = 0

print("Welcome to the word guessing game!\n")
print("Tu pista es: _ _ _ _ _ _")


while guess != palabra_secreta:
    guess = input("¿Cuál es tu conjetura? ").lower()
    numero_intentos += 1
    
    if len(palabra_secreta) == len(guess):
        print("Tu pista es: ")
        for count in range(0, len(guess)):
            print(guess[count].upper() + " ", end="")
        else:
            print("_ ", end="")
    else:
        print("Tu conjetura debe tener el mismo número de letras de la palabra secreta")
        print("Tu pista es: _ _ _ _ _ _")
print(f"Has adivinado la palabra secreta {palabra_secreta} en {numero_intentos} intentos")

