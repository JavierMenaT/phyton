"""edad_primera = int(input("¿Qué edad tienes? "))
altura_primera = int(input("¿Qué altura tienes? "))
acompañante = input("¿Vienes con algún acompañante (SI/NO)? ")

if acompañante.lower() == "si":
    edad_acompañante = int(input("¿Que edad tiene tu acompañante "))
    altura_acompañante = int(input("¿Qué altura tiene tu acompañante "))

    if altura_primera < 36 or altura_acompañante < 36:
        print ("No puede subir al juego")
    else:
        if edad_primera >= 18 or edad_acompañante >= 18:
            print ("Pueden subir al juego")
        else:
            print ("No pueden subir al juego")
else:
    if edad_primera >= 18 and altura_primera >= 36:
        print("Puedes subir al juego")
    else:
        print("No puedes subir al juego")
"""
edad_primera = int(input("¿Qué edad tienes? "))
altura_primera = int(input("¿Qué altura tienes? "))
acompañante = input("¿Vienes con algún acompañante (SI/NO)? ")

if edad_primera >=18 and altura_primera >=36 and acompañante.lower()=="no":
    print("Puedes subir solo!")
else:
    if edad_primera < 18 or altura_primera < 36 and acompañante.lower()=="no":
        print("No puedes subir solo")
    else:
        if edad_primera < 18 or altura_primera >= 36 and acompañante.lower()=="si":
            edad_acompañante = int(input("¿Que edad tiene tu acompañante "))
            altura_acompañante = int(input("¿Qué altura tiene tu acompañante "))
            if edad_acompañante >= 18 and altura_acompañante >=36 and altura_primera >=36:
                print("Pueden subir nop")
            else:
                if edad_acompañante >= 18 and altura_acompañante >=36 and altura_primera >=36 and edad_primera>=18:
                    print("Pueden subir")
            

    
