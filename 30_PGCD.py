a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))

while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a

while b != c:
    if b > c:
        b = b - c
    else:
        c = c - b

print("PGCD : ", c)
