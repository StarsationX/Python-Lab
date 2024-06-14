w = float(input("Weight(Kg) : "))
h = float(input("Height(Meters) : "))

bmi = float(w/h**2)
print("Your BMI is %.2f" % bmi)
if bmi < 18.50:
    print("Too skinny")
elif bmi >= 18.50 and bmi <= 22.99:
    print("Healthy")
elif bmi >= 23 and bmi <= 24.99:
    print("Fat lvl.1")
elif bmi >= 25 and bmi <= 29.99:
    print("Fat lvl.2")
elif bmi >= 30:
    print("Too Fat lvl.3")