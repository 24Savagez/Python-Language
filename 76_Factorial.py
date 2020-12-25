# 5! = 1 x 2 x 3 x 4 x 5
# 0! = 1
import math


def fact(n):
    if n >= 0:
        if n == 0 or n == 1:
            return 1
        else:
            f = 1
            for i in range(2, n+1):
                f = f * i
            return f
    else:
        return math.nan     # not a number


def permutation(n, k):
    # n = 10 (0-9)
    # k = 3
    return fact(n) // fact(n-k)


def combination(n, k):
    # return fact(n) / fact(k)*fact(n-k)
    return permutation(n, k) // fact(k)


if __name__ == '__main__':
    # print(fact(5))
    # print(fact(0))
    # print(fact(-7))
    print(permutation(7, 4))
    # print(combination(4, 3))
