def showBill():
    totalPrice = 0
    print("---- My Food ----")
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])
        totalPrice += int(menuList[number][1])
    print("Total :",totalPrice)

menuList = []

while True:
    menu = input("Input Menu's name :")
    if menu.lower() == "exit":
        break
    else:
        price = input("Enter price :")
        menuList.append([menu,price])


#print(menuList,priceList)

showBill()
