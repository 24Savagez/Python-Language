def price_with_vat(amount):
    vat = amount * 7 / 107  # 107 * 7/107
    price = amount - vat
    t = price, vat  # tuple
    return price, vat
    # return t


# print(price_with_vat(107))
# a = price_with_vat(200)
# print(type(a))
# print(a)
#
# print("Price : ", a[0])
# print("Vat : ", a[1])
#
# p, v = price_with_vat(478)
# print("P :", p)
# print("V : ", v)

def thai_area(sqwa):
    rai = sqwa // 400   # 1 ไร่ = 400 ตารางวา
    ngnn = (sqwa - (rai * 400)) // 100
    wa = sqwa % 100
    return rai, ngnn, wa


# show
a = 956
print(thai_area(a))

r, n, w = thai_area(a)
print(r, n, w, sep="-")
