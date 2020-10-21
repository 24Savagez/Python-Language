for i in range(4):
    for j in range(i):
        print(end=" ")
    for j in range(1):
        print(str(i+1)*2,end="")
    for j in range(1):
        print("*"*(6-2*i),end="")
    for j in range(1):
        print(str(i+1)*2,end="")
    print()
print("-----------")

for i in range(1,5):
    for j in range(3):
        print(i+1*j,end="")
    for j in range(1,i+3):
        print(end="*")
    print()
print("-----------")

for i in range(1,5):
    for j in range(i,9,+4):
        print(j,end="")
    for j in range(1,i+4):
        print(end="*")
    print()
print("-----------")

for i in range(1,5):
    for j in range(i):
        print(end="*")
    for j in range(i,0,-1):
        print(j,end="")
    for j in range(2,i+1):
        print(j,end="")
    print()
print("-----------")