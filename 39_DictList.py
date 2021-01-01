def showBill():
    totalPrice = 0
    print("---- My Food ----")
    for number in range(len(menuBill)):
        print(menuBill[number][0], menuBill[number][1])
        totalPrice += int(menuBill[number][1])
    print("Total :", totalPrice)


# list for fill
menuBill = []
# dictionary
menuList = {'กะเพราหมูกรอบ': 45, 'ผัดซีอิ้ว': 40, 'ข้าวไข่เจียว': 35}

while True:
    menu = input("Input Menu's name :")
    if menu.lower() == "exit":
        break
    else:
        menuBill.append([menu, menuList[menu]])

# print(menuBill)

# call function
showBill()
