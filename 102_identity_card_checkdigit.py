import random


def remover_non_digit(s):
    return [int(c) for c in s if c.isdigit()]


def print_digit(v):
    [print("{:>2} |".format(i), end="") for i in v]
    print()


def chk_digit(c):
    c %= 11
    if c > 9:
        d = c % 10
    else:
        d = (11 - c) % 10
    return d


def random_identity():
    identity_1 = [random.randrange(1, 3) for i in range(1)]
    # listToStr_1 = "".join(map(str, identity_1))

    identity_23 = [random.randrange(96) for j in range(1)]
    # listToStr_23 = "".join(map(str, identity_23))

    identity_4 = [random.randrange(2) for k in range(1)]
    # listToStr_4 = "".join(map(str, identity_4))

    identity_5 = [random.randrange(9) for l in range(1)]
    # listToStr_5 = "".join(map(str, identity_5))

    identity_6_12 = [random.randrange(10) for m in range(7)]
    # listToStr_6_12 = "".join(map(str, identity_6_12))
    return identity_1 + identity_23 + identity_4 + identity_5 + identity_6_12
    # return listToStr_1 + listToStr_23 + listToStr_45 + listToStr_6_12


identity = remover_non_digit(str(random_identity()))
print("=", identity)

print_digit(range(1, 13))
print_digit(identity)
print_digit(range(13, 1, -1))
print("-" * 48)

total = [m * n for m, n in zip(identity, range(13, 1, -1))]
print_digit(total)

last_digit = chk_digit(sum(total))
last_digit = str(last_digit)
print("check_digit = ", last_digit)

listToStr2 = "".join(map(str, identity))
print("identity_number :", listToStr2 + last_digit)















