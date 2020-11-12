def showBill():
    totalPrice = 0
    print("---- My Food ----")
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
        totalPrice += int(priceList[number])
    print("Total :",totalPrice)

menuList = []
priceList = []
while True:
    menu = input("Input Menu's name :")
    if menu.lower() == "exit":
        break
    else:
        price = input("Enter price :")
        menuList.append(menu)
        priceList.append(price)

#print(menuList,priceList)

showBill()



