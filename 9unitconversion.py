"""
File: Unit Conversion
Author: Javier Mena
Class: CSE 110
Number: 9
"""
#get the data
farenheit = float(input("What is the temperature in Farenheit? "))
#operate
celsius = (farenheit - 32) * (5 / 9)
#show
print(f"The temperature in Celsius is: {celsius:.1f} degrees")
#end of program 