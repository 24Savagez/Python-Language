def read_demo(filename):
    # normal
    with open(filename) as f:
        s = f.readlines()
    print(s)
    # use r strip() // right
    s2 = [line.rstrip() for line in s]
    print(s2)


def read_demo2(filename):
    # normal
    with open(filename, mode="r") as f:
        s = f.readlines()
    print(s)
    # use strip()
    s2 = [line.strip() for line in s]
    print(s2)


def read_demo3(filename):
    with open(filename, mode="r") as f:
        s = [line.strip() for line in f]
    print(s)


def read_demo4(filename):
    with open(filename, mode="r") as f:
        s = f.read()
    print(s)
    s2 = s.splitlines()
    print(s2)
    s3 = [a.strip() for a in s2]
    print(s3)


def read_demo5(filename):
    with open(filename, mode="r", encoding="utf8") as f:
        s = f.readlines()
    print(s)
    s2 = [a.strip().split(",") for a in s]
    print(s2)
    s3 = [a.split(",") for a in s]
    print(s3)


filename = "planet2.txt"
# read_demo(filename)
# read_demo2(filename)
# read_demo3(filename)
# read_demo4(filename)
read_demo5(filename)
