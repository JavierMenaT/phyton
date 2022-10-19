"""from readline import set_pre_input_hook
print("For each of these questions, please provide a 1-10 rating:")

loan_size = int(input("How large is the loan? "))
credit = int(input("How good is your credit history? "))
income = int(input("How high is your income? "))
down_payment = int(input("How large is your down payment? "))

# For safety sake, I always like to set the variable to a default value of False
# That way, if for some reason it doesn't get set it in our rules below it will
# not be left "undefined" and cause an error, and I don't like to set the default
# to be True, because I don't want to accidentally give someone a loan!
should_loan = False

if loan_size >= 5:
    if credit >= 7 and income >= 7:
        should_loan = True
    elif credit >= 7 or income >= 7:
        if down_payment >= 5:
            should_loan = True
        else:
            should_loan = False
    else:
        should_loan = False
else: # This means its a small loan
    if credit < 4:
        should_loan = False
    else:
        if income >= 7 or down_payment >= 7:
            should_loan = True
        elif income >= 4 and down_payment >= 4:
            should_loan = True
        else:
            should_loan = False

if should_loan:
    print("The decision is yes. This is a good loan.")
else:
    print("The decision is no. You should not loan this money.")
"""

prestamo = int(input("¿Qué tan grande es el préstamo? "))
credito = int(input("¿Qué tan bueno es su historial de crédito? "))
ingreso = int(input("¿Qué tan alto es su ingreso? "))
deposito = int(input("¿Qué tan grande es su pago inicial? "))

if prestamo >= 5:
    if credito >= 7 and ingreso >= 7:
        print("SI porque cumple la primera condición que el crédito 'Y' el ingreso es mayor que 7")
    elif credito >= 7 or ingreso >= 7:
        if deposito >= 5:
            print("SI porque cumple una de las 2 condiciones (crédito 'O' ingreso mayor a 7) y además el deposito es mayor o igual a 5")
        else:
            print("NO porque aunque el crédito 'O' el ingreso son mayores que 7 el depósito es menor a 5")
    else:
        print("NO porque ni el crédito ni el ingreso son mayores que 7 o en otras palabras porque son menores a 7")
else:
    if credito < 4:
        print("NO porque su historial de crédito es menor que 4")
    else:
        if ingreso >= 7 or deposito >= 7:
            print("SI porque su historial de crédito NO es menor a 4 y su ingreso 'O' su depósito es mayor que 7")
        elif ingreso >= 4 and deposito >= 4:
            print("SI porque su historial de crédito NO es menor a 4 y aunque su ingreso 'O' depósito no sean mayores a 7 si se cumple que el ingreso 'Y' tambien el depósito son mayores o iguales a 4")
        else:
            print("NO porque ni el ingreso o el deposito (es decir, por lo menos 1 de ellos) es mayor que 7 ")