userInput = int(input("Enter Number of your favorite fruits : "))
myfruits = set()
while len(myfruits) < userInput:
    myfruits.add(input("Fruit : "))

print(myfruits)
