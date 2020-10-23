# Test 001
x = int(input("Enter number of Durian(kg.) : "))
y = float(input("Enter purchase pirce(bth) : "))
z = float(input("Enter sale price(bth) : "))

cost = x * y
profit = x * z
net = ((profit*100) / cost)

print("Cost Sale : %.2f"%(cost),"Baht")
print("Profit sale : %.2f"%(profit),"Baht")
print("Total Net.Profit : %.2f"%(net),"%")

