import matplotlib.pyplot as plt

room = ["A", "B", "C"]
boys = [10, 15, 5]
girls = [20, 7, 15]

# plt.bar(room, boys, label="Boys", color="blue")
# plt.bar(room, girls, bottom=boys, label="Girls", color="orange")

plt.stackplot(room, boys, girls, labels=["Boys", "Girls"], colors=["green", "pink"])

plt.xlabel("Room")
plt.ylabel("Total")

plt.legend()

plt.show()
