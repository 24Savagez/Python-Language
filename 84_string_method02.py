# strip / trim
def demo_strip():
    s = "Thailand"
    t = " Thailand "
    v = " Thai land"
    u = t.strip()
    z = v.strip()

    print(s == t)
    print(s == u)
    print(s == z)


def demo_isdigit(p):
    total = 0
    for c in p:
        if c.isdigit():
            # print(c)
            total += int(c)
    return total


def remove_non_digit(s):
    t = ""
    for c in s:
        if c.isdigit():
            t += c
    return t


# plate = "1กท 4567"
# print(demo_isdigit(plate))
phone = "(054)431-456"
card_id = "4404-1234-3838 7788"
print(remove_non_digit(card_id))
print(remove_non_digit(phone))
