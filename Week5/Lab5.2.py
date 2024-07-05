def bmi(kg, cm):
    bmi = kg/(cm/100)**2
    return bmi

def check(w):
    if(w <18.5 ):
        print("Too skinny")
    elif(w >= 18.5 and w <= 22.99):
        print("W BMI You're good")
    elif(w >= 23 and w <= 24.99):
        print("A bit chubby")
    elif(w >= 25 and w <= 29.99):
        print("Nigga you're fat as hell")

kg = int(input("Weight <<< "))
cm = int(input("Height <<< "))
print("Your BMI is >>> %.2f" % bmi(kg, cm))
check(bmi(kg, cm))
