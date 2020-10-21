"""
number = int(input("Enter your numbers :"))
print("*"*number)
print("----------------------------------")

number = 99
while number != 0:
    number = int(input("Enter your numbers : "))
    print("*"*number)
print("----------------------------------")


numbers = int(input())
text = ""
for i in range(numbers):
    text = text + "*"
print(text)
print("----------------------------------")


number = int(input("Enter you number : "))
for i in range(number):
    print(" "*(i)+"*"*(number-i)+str(i+1))
print("----------------------------------")

number = int(input())
for x in range(number):
    text = ""
    for y in range(x+1):
        text += "x"
    print(text)
print("----------------------------------")
"""

number = int(input())
for i in range(number):
    print(" "*(number-i)+"*"*(2*i+1))