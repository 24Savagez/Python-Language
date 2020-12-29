def loop_list():
    flowers = ['calla', 'lilly', 'jasmine', 'forget me not', 'sunflower', 'ivy', 'gypsophila']
    # iterate
    # for f in flowers:
    #     print(f)
    #
    # for i in range(len(flowers)):
    #     print("{}. {}".format(i+1, flowers[i]))

    for i, e in enumerate(flowers):
        print("{}. {}".format(i+1, e))


def loop_list2():
    countries = [
        ("th", "Thailand", "ไทย"),
        ("jp", "japan", "ญี่ปุ่น"),
        ("kr", "korea", "เกาหลีใต้")
    ]
    # for country in countries:
    #     # print(country)
    #     print(country[2])

    for i, country in enumerate(countries):
        print("{} {}".format(i+1, country[2]))


loop_list2()
