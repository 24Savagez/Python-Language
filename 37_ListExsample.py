def show_bill():
    total_price = 0
    print("---- My Food ----")
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])
        total_price += int(priceList[number])
    print("Total :", total_price)


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

# print(menuList,priceList)

show_bill()
