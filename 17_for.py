print(list(range(10)))
print("---------------------------------------")

for i in range(10):
    print(i+1,"Hello","\t","FirstOnez")
print("---------------------------------------")


inputRound = int(input("Please Enter number :"))
sum = 0
for x in range(inputRound):
    inputNumber = int(input("x"+str(x+1)+" : "))
    sum += inputNumber
print("Total :",sum)
print("---------------------------------------")

start = int(input("Start :"))
step =  int(input("Step : "))

for i in range(5):
    print(start + step*i ,end=" ")