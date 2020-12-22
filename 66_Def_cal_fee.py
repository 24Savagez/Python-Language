# type 1
def basic():
    # input
    amt = 45000

    # process
    fee = 0
    if amt <= 5000:
        fee = 0
    elif 5000 < amt <= 30000:
        fee = 2
    elif 30000 < amt <= 100000:
        fee = 5
    else:
        fee = 10

    # output
    print("fee :", fee)


# type 2
def basic2():
    # input
    amt = float(input("Transfer amount : "))
    fee = 0

    # process
    if amt > 100000:
        fee = 10
    elif amt > 30000:
        fee = 5
    elif amt > 5000:
        fee = 2
    else:
        fee = 0

    # output
    print(fee)


# dunder = double underscore
# special variables
# main() in C-language
if __name__ == '__main__':
    basic2()

# type main and tap 1 time
