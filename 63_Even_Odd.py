def is_even(n):
    return True if n % 2 == 0 else False


def is_odd(n):
    return not(is_even(n))


number = int(input("Enter number :"))

print("Even", is_even(number))
print("Odd", is_odd(number))
