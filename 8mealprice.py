"""
File: Meal price calculator
Author: Javier Mena
Class: CSE 110
Number: 8
"""

#get the data 
child_meal=float(input("What is the price of the child´s meal: "))
adult_meal=float(input("What is the price of the adult´s meal: "))
number_children=int(input("How many children are there: "))
number_adults=int(input("How many adults are there: "))
sale_tax=float(input("What is the sales tax rate: "))

print()
#do the calculations and show the results
subtotal=child_meal*number_children+adult_meal*number_adults
subtotal_with_tax=(subtotal*sale_tax)/100
total=subtotal+subtotal_with_tax
print(f"Subtotal: ${subtotal}")
print(f"Sales Tax: ${subtotal_with_tax}")
print(f"Total: ${total}")

print()
#show the pay and change
payment_amount=float(input("What is the payment amount: $"))
change=payment_amount-total
print(f"Change: ${change}")
