def demo_reader():
    # open
    f = open("flowers.txt")
    # read
    data = f.read()
    print(data)
    # close
    f.close()


def demo_readline():
    # open
    f = open("flowers.txt")
    # read
    data = f.readline()
    print(data)
    data2 = f.readline()
    print(data2)
    # close
    f.close()


def demo_readlines():
    # open
    f = open("flowers.txt")
    # read
    data = f.readlines()
    print(data)
    # close
    f.close()


def demo_readline2():
    # open
    f = open("flowers.txt")
    # read
    for i in range(3):
        print(f.readline(), end="")
    # close
    f.close()


def demo_readlines2():
    # open
    f = open("flowers.txt")
    # read
    for line in f:
        print(line.capitalize(), end="")
    # close
    f.close()


# demo_reader()
# demo_readline()
# demo_readlines()
# demo_readline2()
demo_readlines2()
