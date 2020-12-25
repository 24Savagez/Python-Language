# s = "first"
# print(s.capitalize())
# print(s.upper())
#
# t = "Onez"
# print(t.lower())

def demo_upper():
    choice = input("[M]ale, [F]emale : ")
    if choice.upper() == "M":
        print("male")
    else:
        print("female")


def demo_title():
    s = "the land of smile"
    print(s.title())


def demo_split():
    s = "the land of smile"
    a = (s.split())
    print(a)
    print(a[1])
    t = "thailand, 5, 7, 3"
    b = t.split(",")
    print(b)
    x = "1920x1080"
    p = x.split("x")
    print(p)
    w, h = x.split("x")
    print(w, h)


def demo_split_app():
    first_name, last_name = input("enter your full name : ").split()
    print("first name : ", first_name.capitalize())
    print("last name : ", last_name.capitalize())
    print("Hello {}. How are you?".format(first_name.capitalize()))


# demo_upper()
# demo_title()
# demo_split()
demo_split_app()
