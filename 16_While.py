usernameInput = ()
passwordInput = ()

while usernameInput != "admin" or passwordInput != "1234":

    usernameInput = input("Username : ")
    passwordInput = input("Password : ")

    if usernameInput == "admin" and passwordInput == "1234":
        print("Done !")
    else:
        print("Wrong,Try again...")
        print()