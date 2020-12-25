# point = 1, 7
# print(point[0])
# print(point[1])
#
# point2 = (1, 7)
# print(point[0])
# print(point[1])
#
# th = "Thailand", 5, 10, 15
# print(th[1]+th[2]+th[3])
#
# monsters = ("pikachu", "bulbasaur", "eevee")
# print(monsters[1])

def distance(pointA, pointB):
    return ((pointA[0]-pointB[0]) ** 2 + (pointA[1]-pointB[1]) ** 2) ** 0.5


def distance2(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


# distance
pointA = 1, 7
pointB = 1, 10
print(distance(pointA, pointB))

# distance2
print(distance2(1, 7, 1, 10))

# immutable สร้างมาแล้ว แก้ไขค่าไม่ได้

