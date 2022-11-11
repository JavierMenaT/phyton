print("Ingrese varios números, para terminar ingrese el 0")

numeros = []
numero = -1

while numero != 0:
    numero = int(input("Ingrese un número: "))

    if numero != 0:
        numeros.append(numero)
print()
print("Tus números son los siguientes: ")

for numero in numeros:
    print(numero)

    