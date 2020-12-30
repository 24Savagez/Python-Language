def km_mile(k):
    return k * 0.621371


# list comprehensions
def v1():
    n = [km_mile(i) for i in range(1, 11)]
    p = [(i, km_mile(i)) for i in range(1, 11)]
    print(n)
    print(p)


def v2():
    flowers = ("lily", "carnation", "iris", "sunflower", "ivy")
    n = [f.capitalize() for f in flowers]
    p = [f.capitalize() for f in flowers if f[0] == "i"]
    q = [f.capitalize() if f[0] == "i" else f for f in flowers]
    print(n)
    print(p)
    print(q)


def v3():
    az = [chr(i) for i in range(ord("A"), ord("Z")+1)]
    az2 = [chr(i) for i in range(ord("A"), ord("Z")+1) if chr(i) not in "OI"]
    print(az)
    print(az2)
    a = "".join(az)
    print(a)


# v1()
# v2()
v3()

