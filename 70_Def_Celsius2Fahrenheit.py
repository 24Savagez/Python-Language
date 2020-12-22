def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (9/5)


# void function
def temperature_table():
    for c in range(0, 101, 5):
        f = celsius_to_fahrenheit(c)
        print("{} C = {} F".format(c, f))
    # return None


def menu():
    print("1. convert Celsius to Fahrenheit")
    print("2. convert Fahrenheit to Celsius")
    print("3. display temperature table")
    n = input("Enter choice : ")
    if n == "1":
        celsius = float(input("Enter degree in Celsius : "))
        print("{} C = {} F".format(celsius, celsius_to_fahrenheit(celsius)))
    elif n == "2":
        fahrenheit = float(input("Enter degree in Fahrenheit : "))
        print("{} F = {} C".format(fahrenheit, fahrenheit_to_celsius(fahrenheit)))
    elif n == "3":
        temperature_table()


# f = celsius_to_fahrenheit(100)
# print(f)
# temperature_table()
menu()
