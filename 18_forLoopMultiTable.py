'''
2 x 1 = 2
2 x 2 = 4

print("2 x 1 = 2")
print("2 x 2 = 4")
print("--------------------------")

x = 1
y = 2*x
print("2 x",x,"=",y)
x = x+1
y = 2*x
print("2 x",x,"=",y)
print("--------------------------")

for x in range(12):
    x = x+1
    y = 2*x
    print("2 x",x,"=",y)
print("--------------------------")

for x in range(12):
    print("2 x",x+1,"=",2*(x+1))
print("--------------------------")
'''

for x in range(11):
    for y in range(12):
        print(str(x+2),"x",y+1,"=",(x+2)*(y+1))
    print()
print("--------------------------")

""""
for i in range(1,13):
    print("2 x",i,"=",2*i)
print("--------------------------")
"""
"""
for i in range(2,13):
    for j in range(1,13):
        print(i,"x",j," = "+str(i*j))
    print()
print("--------------------------")
"""