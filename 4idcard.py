#import email
#from turtle import title
"""
File: ID Card
Author: Javier Mena
Class: CSE 110
"""
print("Please insert the following information \n")
first=input("First name: ")
last=input("Last name: ")
email=input("Email address: ")
phone=input("Phone number: ")
jobtitle=input("Job title: ")
idnumber=input("ID number: ")
print("\nThe ID card is: ")
print("---------------------------------")
print(last.upper()+", "+first.capitalize())
print(jobtitle.title())
print("ID: "+idnumber+"\n")
print(email.lower())
print(phone)
print("---------------------------------")