def write_demo():
    # name file
    f = open(r"demo3.txt", "w", encoding="utf8")
    # write
    f.write("hello python\n")
    f.write("I love python\n")
    f.write("line 3\n")
    f.write("I love ไพธอน\n")
    # close
    f.close()


def write_context_mgr():
    # name file
    with open(r"demo4.txt", "w", encoding="utf8") as f:
        # write
        f.write("hello python\n")
        f.write("I love python\n")
        f.write("line 3\n")
        f.write("I love ไพธอน\n")
        f.write("จุฑายุ อฑิตยวงค์\n")


def write_list():
    menu = ["mocha", "latte",
            "espresso", "macchiato"]
    with open("menu.txt", "w", encoding="utf8") as f:
        for m in menu:
            # f.write(m + "\n")
            f.write("{}\n".format(m.capitalize()))


# write_demo()
# write_context_mgr()
write_list()
