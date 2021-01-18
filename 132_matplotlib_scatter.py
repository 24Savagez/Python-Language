import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1.2, 3, 2.3, 4.5, 3]

size = [100, 200, 800, 100, 300]
color = ["red", "orange", "green", "magenta", "yellow"]
plt.scatter(x, y, s=size, c=color)

plt.show()
