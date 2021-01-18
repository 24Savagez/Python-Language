import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(10, 2.5, 5000)

plt.hist(data, bins=30)

plt.show()
