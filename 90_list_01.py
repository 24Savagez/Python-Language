def demo_basic_operation():
    flowers = ["calla", "lilly", "jasmine"]
    print(flowers)

    # add
    flowers = flowers + ["forget me not", "sunflower", "ivy", "gypso"]
    print(flowers)

    # delete
    del flowers[1]
    print(flowers)

    # remove
    flowers.remove("jasmine")
    print(flowers)

    # sort name
    sorted_flowers = sorted(flowers)
    print(sorted_flowers)

    # sort name
    print(flowers)
    flowers.sort()
    print(flowers)

    # add append
    flowers.append("carnation")
    print(flowers)


def demo():
    flowers = ['calla', 'lilly', 'jasmine', 'forget me not', 'sunflower', 'ivy', 'gypso']
    # slice
    print(flowers[1:4])  # [inclusive:exclusive]
    print(flowers[-1])
    print(flowers[-1:-4:-1])
    print(flowers[:3])
    print(flowers[2:])


demo()
