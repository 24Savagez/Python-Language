import matplotlib.pyplot as plt

# data
product1 = [10, 20, 30, 40, 50]
product2 = [15, 30, 10, 20, 60]
month = [1, 2, 3, 4, 5]

# show plot
plt.plot(month, product1, color="c", marker="s", linestyle=":")
plt.plot(month, product2, "ms-.")

# title
config = {"size": 25, "color": "green"}
plt.title("Top Sale 2020", config, loc="left")

# set label
data = {"size": 20, "color": "blue", "backgroundcolor": "yellow"}
plt.xlabel("Month", size=20, color="red", backgroundcolor="yellow")
plt.ylabel("Sales", data)

# save picture
# plt.savefig("export1.png", transparent=True)

plt.show()
