#---------------------------Esta mi solución------------------------ 
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

#---------------------otra solución---------------------------------
dato=int(input("What is your grade porcent? "))

if dato >= 90:
    letra = "A"
elif dato >= 80:
    letra = "B"
elif dato >= 70:
    letra = "C"
elif dato >= 60:
    letra = "D"
else:
    letra = "F"  
# -------------------Ejercicio completado el desafío------------------
signo = ""
residuo = dato % 10
if residuo >= 7:
    signo = "+"
elif residuo < 3:
    signo = "-"
else:
    signo = ""

print(f"Your letter grade is: {letra}{signo}")
if dato >=70:
    print("Congratulations! you passed the class!")
else:
    print("Stay focus and you'll get it next time")


