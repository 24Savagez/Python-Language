def ticket(age, is_local):
    # ternary
    return 0 if (age <= 5 or age >= 60) and is_local else 100


print(ticket(20, True))

# even or odd in ternary
number = int(input("Enter you number : "))
print("Even" if number % 2 == 0 else "Odd")
