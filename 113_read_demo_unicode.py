def demo_reader():
    # open
    with open("flowers.txt", mode="r") as f:
        # name file
        print(f.name)
        # mode read = r
        print(f.mode)
        # read auto close
        data = f.read()
        print(data)


def demo_reader2():
    # open
    # use \\
    # with open("C:\\Users\\JaiDog\\Documents\\GitHub\\Python-Language\\All_docs\\flowers.txt", mode="r") as f:
    # use r
    # with open(r"C:\Users\JaiDog\Documents\GitHub\Python-Language\All_docs\flowers.txt", mode="r") as f:
    # use /
    with open("C:/Users/JaiDog/Documents/GitHub/Python-Language/All_docs/flowers.txt", mode="r", encoding="utf8") as f:
        # name file
        print(f.name)
        # mode read = r
        print(f.mode)
        # read auto close
        data = f.read()
        print(data)


def demo_reader_unicode():
    # open
    with open("C:/Users/JaiDog/Documents/GitHub/Python-Language/All_docs/province.txt", mode="r", encoding="utf8") as f:
        # name file
        print(f.name)
        # mode read = r
        print(f.mode)
        # read auto close
        data = f.read()
        print(data)


def demo_reader_unicode2():
    # open
    with open("C:/Users/JaiDog/Documents/GitHub/Python-Language/All_docs/province.txt", mode="r", encoding="utf8") as f:
        # i = 1
        # for line in f:
        #     print("{}. {}".format(i, line), end="")
        #     i += 1
        for i, line in enumerate(f):
            print("{}. {}".format(i+1, line), end="")
            i += 1


# demo_reader()
# demo_reader2()
# demo_reader_unicode()
demo_reader_unicode2()
