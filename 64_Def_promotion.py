def promotion(pax, per_head=100, come=4, pay=3):
    # come 4 , pay 2
    # come 5 , pay =?
    # per_head = 100
    # 200 + 100
    return (pax // come) * (pay * per_head) + (pax % come) * per_head


# set you promotion
pax = int(input("Enter number customer come : "))
print("Total pay :", promotion(pax))
