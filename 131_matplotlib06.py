import matplotlib.pyplot as plt

# data
student = [10, 20, 40, 30, 60]
course = ["PHP", "Java", "Python", "C#", "Node js"]

# plot circle
color = ["purple", "red", "cyan", "yellow", "green"]
exp = [0, 0.1, 0, 0.2, 0]
plt.pie(student, labels=course, autopct="%.1f%%",
        colors=color, shadow=True, explode=exp,
        startangle=0)

# show plot
plt.show()
