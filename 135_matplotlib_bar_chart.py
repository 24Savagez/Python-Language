import matplotlib.pyplot as plt

course = ["Python", "Java", "C#"]
score = [80, 75, 50]

plt.bar(course, score)
plt.xlabel("course")
plt.ylabel("score")
plt.title("Score Midterm")

plt.show()
