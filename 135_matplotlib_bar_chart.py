import matplotlib.pyplot as plt

course = ["Python", "Java", "C#"]
score = [80, 75, 50]
color = ["green", "orange", "blue"]

# bar vertical
# plt.bar(course, score, color=color, width=0.6,
#         edgecolor="black", linewidth=2)

# bar horizontal
plt.barh(course, score, color=color,
         edgecolor="black", linewidth=2)

plt.xlabel("score")
plt.ylabel("course")
plt.title("Score Midterm")

plt.show()
