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

plt.legend(["Mouse", "Keyboard"],
           title="product", title_fontsize="large",
           loc="best",
           fontsize="x-small",
           facecolor="pink", edgecolor="gold",
           borderpad=2,
           labelspacing=1
           )
plt.show()




