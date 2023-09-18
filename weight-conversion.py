#converting kg to pounds
weight = int(input("Weight: "))
unit = input("(L)bs or (K)g: ")

if unit.upper() == "K":
    print(weight * 0.45)
elif unit.upper() == "L":
    print(weight / 0.45)



