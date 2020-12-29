def v1():
    for i in range(1, 11):
        print(i, i * 0.621371)


# list comprehensions
def v2():
    [print(i, i * 0.621371) for i in range(1, 11)]
    m = [(i * 0.621371) for i in range(1, 11)]
    n = [km_mile(i) for i in range(1, 11)]
    print(m)
    print(n)


# lambda
def v3():
    m = list(map((lambda i: i * 0.621371), range(1, 11)))
    print(m)


def km_mile(k):
    return k * 0.621371


# list comprehensions
def sum_total():
    [print(i) for i in range(1, 101) if (i % 2 == 0)]


# v2()
sum_total()

