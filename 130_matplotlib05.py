import matplotlib.pyplot as plt
import numpy as np

product1 = [10, 20, 30, 40, 50]
product2 = [15, 30, 10, 20, 60]
month = [1, 2, 3, 4, 5]

plt.plot(month, product1, "gs-.")
plt.plot(month, product2, "rs-.")

data = {"size": 20, "color": "red", "backgroundcolor": "yellow"}
plt.xlabel("Month", data)
plt.ylabel("Sale", data)

config = {"size": 20, "color": "blue"}
plt.title("Top Sale 2020", config, loc="left")

plt.text(1.8, 32, "Point1", size="large", color="green")
plt.text(3.8, 15, "Point2", size=15, color="red")

plt.show()
