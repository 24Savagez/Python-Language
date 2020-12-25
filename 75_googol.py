def demo1():
    # Google (googol) = 1e100
    print("1"+"0" * 100)

    # string format
    print("1{0}".format("0" * 100))

    # f-string (Python 3.6+)
    print(f'1{"0" * 100}')


def demo2():
    print("1", end='')
    for i in range(100):
        print("0", end='')


def repeat(ch, time):
    for i in range(time):
        print(ch, end='')


def repeat2(ch, time):
    s = ""
    for i in range(time):
        s += ch
    return s


# repeat1
print("1", end="")
repeat("0", 10)

# repeat2
print('1' + repeat2("0", 100))
