"""first=float(input("What is the first number?: "))
second=float(input("What is the second number?: "))
if first>second:
    print("The first number is greater")
    print("The numbers are not equal")
    print("The second number is not greater")
elif first==second:
    print("The first number is not greater")
    print("The numbers are equal")
    print("The second number is not greater")
elif first<second:
    print("The first number is not greater")
    print("The numbers are not equal")
    print("The second number is greater")
print()
fav_animal=input("What's your favorite animal?: ")
if fav_animal.lower()=="bear":
    print("That's my favorite animal too!")
else:
    print("That one is not may favorite.")"""

"""
File: If Statements
Author: Javier Mena
Class: CSE 110
Number: 11 
"""
#get data el tipo de dato en este ejercicio es entero (int) 
first=int(input("What is the first number?: "))
second=int(input("What is the second number?: "))

#do the firts comparison
if first > second:
    print("The first number is greater") #si es verdad imprimirá esto, caso contrario imprimirá la segunda línea y procedera a hacer las demas comparaciones
else:
    print("The first number is not greater")
if first == second:
    print("The numbers are equal")
else:
    print("The numbers are not equal")
if first < second:
    print("The second number is greater")
else:
    print("The second number is not greater")

print()

fav_animal = input("What's your favorite animal?: ")
if fav_animal.lower() == "cougar": #el dato ingresado por el usuario lo convertimos a minúsculas con la función .lower()
    print("That's my favorite animal too!")
else:
    print("That one is not may favorite.")
