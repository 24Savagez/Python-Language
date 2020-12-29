# contacts = ["peter", "parker", 21]
# print(contacts)

# scores = [10, 15, 7, 8]
# # sum
# print(sum(scores))
# # length
# print(len(scores))
# # average
# print(sum(scores)/len(scores))

# multidimensional list
def multidim_list():
    countries = [
        ("th", "Thailand", "ไทย"),
        ("jp", "japan", "ญี่ปุ่น"),
        ("kr", "korea", "เกาหลีใต้")
    ]
    print(countries)
    print(countries[1])
    print(countries[1][1])
    print(countries[0][2])


def multidim_list2():
    menus = [
        ["mocha", [20, 30, 40]],
        ["latte", [40, 50, 55]],
        ["espresso", [120, 130, 140]],
        ["water", [10]]
    ]
    print(menus)
    print(menus[2][1])
    print(menus[2][1][1])


multidim_list2()

