# function calculate rectangle
def rectangle(w, h):
    area = w * h
    return area


def triangle(w, h):
    return 0.5 * (w * h)


# menu
print("1. rectangle")
print("2. triangle")

# main entry point
n = input("Please select options : ")
width = int(input("Width : "))
height = int(input("Height : "))

# call function
if n == '1':
    print("rectangle area", rectangle(width, height))
else:
    print("triangle area", triangle(width, height))
