def BMI(w,h):
    h1  = h / 100
    b = w / (h1 * h1)
    print("Your BMI is %.2f" %b)
    return b

w = float(input("Weight(KG) >>> "))
h = float(input("Height(CM) >>> "))

b = BMI(w,h)

if b < 18.50:
    print("Too skinny")
elif b >= 18.50 and b <= 22.99:
    print("Healthy")
elif b >= 23 and b <= 24.99:
    print("Fat lvl.1")
elif b >= 25 and b <= 29.99:
    print("Fat lvl.2")
elif b >= 30:
    print("Too Fat lvl.3")