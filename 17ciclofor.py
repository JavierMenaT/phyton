
"""Mostrar los elementos de una lista
color = ["red", "blue", "green", "yellow"]

for colors in color:
    print(colors)"""

#Mostrar los elementos de una lista desde el 1 al 8
#----------1era FORMA----------
#numbers = [1,2,3,4,5,6,7,8]

#for number in numbers:
#    print(number)

#Mostrar los elementos de una lista desde el 1 al 8, pero usando la función range()
#----------2da FORMA----------
rango = range(1,9)

for numeros in rango:
    print(numeros)

#Mostrar los elementos de una lista desde el 2 al 2, pero contando de 2 en 2

rango = range(2, 22, 2)

for pares in rango:
    print(pares)