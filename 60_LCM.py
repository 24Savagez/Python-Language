# least common multiple
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))

# find minimum of numbers
'''
if a < b and a < c:
    min_number = a
elif b < a and b < c:
    min_number = b
else:
    min_number = c
'''

# use function min()
min_number = min(a, b, c)

# solution
while True:
    if min_number % a == 0 and min_number % b == 0 and min_number % c == 0:
        print(min_number)
        break
    min_number += 1
