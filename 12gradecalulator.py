#---------------------------THIS IS MY SOLUTION------------------------ 
nota=int(input("What is your grade porcent? "))

if nota >= 90:
    print("Your letter grade is A")
elif nota >= 80:
    print("Your letter grade is B")
elif nota >= 70:
    print("Your letter grade is C")
elif nota >= 60:
    print("Your letter grade is D")
else:
    print("Your letter grade is F")   
    
if nota >=70:
    print("Congratulations! you passed the class!")
else:
    print("Stay focus and you'll get it next time")

#---------------------TEACHER SOLUTION---------------------------------
grade=int(input("What is your grade porcent? "))

if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"  

print(f"Your letter grade is: {letter}")

if grade >= 70:
    print("Congratulations! You passed the class!")
else:
    print("Stay focused and you'll get it next time!")
# -------------------Ejercicio completando el desafío------------------
signo = ""
residuo = grade % 10
if residuo >= 7:
    signo = "+"
elif residuo < 3:
    signo = "-"
else:
    signo = ""

print(f"Your letter grade is: {letter}{signo}")
if grade >=70:
    print("Congratulations! you passed the class!")
else:
    print("Stay focus and you'll get it next time")


