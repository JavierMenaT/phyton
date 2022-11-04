#Recorrer una palabra y mostrarla verticalmente cambiando la letra ingresada por el usuario si la hay por una mayúscula 
palabra = "commitment"
letra_favorita = input("¿Cuál es tu letra favorita? ")
for letra in palabra:
    if letra.lower() == letra_favorita.lower():
        print(letra.upper())
    else:
        print(letra.lower())
print()

#Recorrer una palabra y mostrarla horizontalmente cambiando la letra ingresada por el usuario si la hay por una mayúscula 
palabra = "commitment"
letra_favorita = input("¿Cuál es tu letra favorita? ")
for letra in palabra:
    if letra.lower() == letra_favorita.lower():
        print(letra.upper(), end ="")
    else:
        print(letra.lower(), end ="")
print()

#Recorrer una palabra y mostrarla horizontalmente cambiando la letra ingresada por el usuario si la hay por un guión 
palabra = "commitment"
letra_favorita = input("¿Cuál es tu letra favorita? ")
for letra in palabra:
    if letra.lower() == letra_favorita.lower():
        print("_", end ="")
    else:
        print(letra.lower(), end ="")
print()
