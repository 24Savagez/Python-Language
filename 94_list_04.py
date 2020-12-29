def demo():
    flowers = ['calla', 'lilly', 'jasmine', 'forget me not', 'sunflower', 'ivy', 'gypsophila']
    # is_exits = "daisy" in flowers
    # is_exits = "lilly" in flowers
    # print(is_exits)

    # find name from index
    # print(flowers.index("lilly"))
    # print(flowers.index("daisy"))

    # capitalize 1 word
    # flowers[2] = "Jasmine"
    # print(flowers)

    # capitalize all word
    for i in range(len(flowers)):
        flowers[i] = flowers[i].capitalize()
    print(flowers)

    # clear all in list
    flowers.clear()
    print(flowers)


def demo_append():
    countries = [
        ("th", "Thailand", "ไทย"),
        ("jp", "japan", "ญี่ปุ่น"),
        ("kr", "korea", "เกาหลีใต้")
    ]
    print(countries)
    # append
    fr = ("fr", "france", "ฝรั่งเศส")
    countries.append(fr)
    print(countries)

    # insert
    us = ("us", "usa", "อเมริกา")
    countries.insert(2, us)
    print(countries)

    # append
    countries.append(("sg", "singapore", "สิงคโปร์"))
    print(countries)


# demo_append()
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(alphabet)

a = [0] * 10
print(a)

b = [1, 3] * 5
print(b)

