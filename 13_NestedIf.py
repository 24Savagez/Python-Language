if True:
    print("Hello Welcome !")
    if True:
        print("Yo! Ms.F")
        if True:
            print("WTF")
print("------------------------------------------------")

usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == "admin" and passwordInput == "1234":
    print("Done !")

    print("------iShop------")
    print("1.Vat Calculator")
    print("2.Price Calculator")
    userSelected = int(input(": "))

    if userSelected == 1:
        price = int(input("Price(THB) : "))
        vat = 0.07
        result = price * vat
        print("You must pay Vat :" + format(result, '.2f'))
    elif userSelected == 2:
        price = int(input("Price(THB) : "))
        vat = 1.07
        result = price * vat
        print("You must pay Net :", result)
print("------------------------------------------------")
