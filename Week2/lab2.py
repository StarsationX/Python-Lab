x = int(input("Score : "))

if x >= 0 and x <= 100:
    if x >= 80 and x <= 100:
        print("A")
    elif x >= 70 and x <= 79:
        print("B")
    elif x >= 60 and x <= 69:
        print("C")
    elif x >= 50 and x <= 59:
        print("D")
    elif x >= 0 and x <= 49:
        print("F")
else:
    print("Please input 0 - 100")