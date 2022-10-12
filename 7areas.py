#first solution
"""
side=int(input("What is the lenght of a side of the square: "))
square=side*side
print("The area of the square is: ",square)
"""
#second solution
"""
side=input("What is the lenght of a side of the square: ")
square=int(side)
area_square=str(square*square)
print("The area of the square is: "+area_square)
"""
"""
File:  Calculation of areas
Author: Javier Mena
Class: CSE 110
Number: 7
"""
#final solution area of the square
from turtle import width
print("AREA OF A SQUARE")
lenght_square=input("What is the lenght of a side of the square?: ")
side=float(lenght_square)
area_square=str(side**2)
print("The area of the square is: "+area_square)
print()

#area of the rectangle
print("AREA OF A RECTANGLE")
lenght_rectangle=input("What is the lenght of the rectangle?: ")
width_rectangle=input("What is the width of the rectangle?: ")
lenght=float(lenght_rectangle)
width=float(width_rectangle)
area_rectangle=str(lenght*width)
print("The area of the rectangle is: "+area_rectangle)
print()

#area of the rectangle
print("AREA OF A CIRCLE")
radio_circle=input("What is the radio of the circle?: ")
radio=float(radio_circle)
area_circle=str(radio**2*3.14)
print("The area of the circle is: "+area_circle)