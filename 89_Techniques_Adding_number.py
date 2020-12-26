# sum 1 + 2 + 3 + 4 + ... + n
i = 1
n = 10
total = ((n * (n+1))/2) - ((i - 1) * i / 2)
print(total)

# even number
# sum 2 + 4 + 6 + 8 + ... + n
i = 2
n = 100
step = 2
# total2 = (step * (n/i) * (n/i+1))/step
total2 = n/i * (n/i+1)
print(total2)

# odd number
# sum 1 + 3 + 5 + 7 + ... + n
i = 1
n = 13
step = 2
total3 = ((n+1)/2 * ((n+1)/2+1))-((n+1)/2)
print(total3)

