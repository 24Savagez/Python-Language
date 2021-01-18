import matplotlib.pyplot as plt

# data
product1 = [10, 20, 30, 40, 50]
product2 = [15, 30, 10, 20, 60]
month = [1, 2, 3, 4, 5]

# show plot
plt.plot(month, product1, color="c")
plt.plot(month, product2, color="m")

# set label
plt.xlabel("Month")
plt.ylabel("Sales")

# save picture
# plt.savefig("export1.png", transparent=True)

plt.show()
