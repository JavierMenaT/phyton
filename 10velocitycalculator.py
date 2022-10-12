"""
File: Velocity calculator
Author: Javier Mena
Class: CSE 110
Number: 10
"""

from cmath import sqrt
import math

print("Welcome to the velocity calculator. Please enter the following: ")
print()
m=float(input("Mass (in Kg): "))
g=float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
t=float(input("Time (in seconds): "))
p=float(input("Density of the fluid (in Kg/m^3, 1.3 for air, 1000 for water): "))
A=float(input("Cross sectional area (in m^2): "))
C=float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))
print()

c = 1 / 2 * p * A * C
#first formula
velocity=(math.sqrt((m * g) / c)) * (1 - math.exp((-math.sqrt(m  *g * c) / m) * t))

#fórmula usando el número e y los operadores para elevar a una potencia
velocity2=(math.sqrt((m * g ) / c)) * (1 - math.e**((-math.sqrt(m * g * c) / m) * t))
#e=math.exp(2)

print(f"The inner value of c is: {c:.3f}")
print(f"The velocity after {t} seconds is: {velocity:.3f} m/s")
print(f"The velocity 2 after {t} seconds is: {velocity2:.4f} m/s")
#end of file
