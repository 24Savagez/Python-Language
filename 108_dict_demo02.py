def demo2():
    m = {"th": [5, 3, 7],
         "sg": [3, 1, 2]
         }
    print(m)
    print(m["th"])
    print(m["th"][0])
    print(m["th"][0] + m["th"][1] + m["th"][2])


def demo3():
    m = {
        "th": {"g": 5, "s": 3, "b": 7},
        "sg": {"g": 3, "s": 1, "b": 2}
    }
    print(m)
    print(m["th"])
    print(m["th"][0])
    print(m["th"][0] + m["th"][1] + m["th"][2])
