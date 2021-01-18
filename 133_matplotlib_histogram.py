import matplotlib.pyplot as plt

age = [10, 15, 20, 15, 15, 15, 10, 20, 34, 15, 10, 25, 25, 25, 20, 30, 40, 20, 10, 15, 20, 30]

plt.hist(age)

plt.xlabel("Age", color="red")
plt.ylabel("Count", color="green")

plt.title("Total Age")

plt.show()
