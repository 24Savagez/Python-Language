# max or min:
findValue = input("What Do you to find (max or min)? : ")

# input 3 Numbers for find max or equal
a = float(input("Enter your number1 :"))
b = float(input("Enter your number2 :"))
c = float(input("Enter your number3 :"))
print()

if findValue == "max":
    # algorithm max Value
    if a > b:
        if a > c:
            print(": A is max")
        elif a == c:
            print(": AC are max")
        else:
            print(": C is max")
    elif a > c:
        if b > a:
            print(": B is max")
        elif a == b:
            print(": AB are max")
        else:
            print(": A is max")
    elif b == c:
        if b == a:
            print(": ABC are equal")
        else:
            print(": BC are max")
    elif a < c:
        if c > b:
            print(": C is max")
        else:
            print(" B is max")

if findValue == "min":
    # algorithm for min value
    if a < b:
        if a < c:
            print(": A is min")
        elif a == c:
            print(": AC are min")
        else:
            print(": C is min")
    elif a < c:
        if b < a:
            print(": B is min")
        elif a == b:
            print(": AB are min")
        else:
            print(": A is min")
    elif b == c:
        if b == a:
            print(": ABC are equal")
        else:
            print(": BC are min")
    elif a > c:
        if c < b:
            print(": C is min")
        else:
            print(": B is min")
