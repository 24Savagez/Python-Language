import csv


def demo1():
    # w = write // a = append
    with open("some.csv", "a", newline="", encoding="utf8") as f:
        fw = csv.writer(f)
        # fw.writerow(["one", "two",
        #              "three"])
        # fw.writerow(("lily", "carnation", "rose"))
        # fw.writerow(["th", "Thailand", "ประเทศไทย"])
        fw.writerow(["a", "b", "c"])


def demo2():
    menus = [
        ["mocha", 30, 40, 50],
        ["latte", 40, 50, 60],
        ["espresso", 50, 60, 70]
    ]
    with open("some2.csv", "w", newline="", encoding="utf8") as f:
        fw = csv.writer(f, delimiter="|",
                        quoting=csv.QUOTE_NONNUMERIC)
        fw.writerow(["menu", "s", "m", "l"])
        fw.writerows(menus)


demo1()
# demo2()
