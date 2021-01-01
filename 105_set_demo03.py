def demo_loop():
    s = {"apple", "banana", "mango", "cherry"}
    a = list(s)
    a.sort()
    for f in a:
        print(f)


def demo_loop2():
    countries = {
        ("th", "Thailand"),
        ("jp", "Japan"),
        ("kr", "Korea")
    }
    # print(countries)
    # for c in countries:
    #     print(c[1])
    # for countries_id, countries_name in countries:
    #     print(countries_name)

    # for i, (countries_id, countries_name) in enumerate(countries):
    #     print("{}. {} {}".format(i+1, countries_id, countries_name))

    if ("jp", "Japan") in countries:
        print("found")
    else:
        print("not found")


def immutable_set():
    # frozenset
    fz = frozenset(["lily", "carnation"])
    print(fz)
    print(type(fz))


# demo_loop2()
immutable_set()
