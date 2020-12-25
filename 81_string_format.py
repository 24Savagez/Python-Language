def demo():
    first_name = "First"
    last_name = "Onez"
    age = 20

    print(first_name, last_name, age)
    print("{} {} age:{}".format(first_name, last_name, age))
    print("{0} {1} age:{2}".format(first_name, last_name, age))
    print("{1} , {0} age:{2}".format(first_name, last_name, age))   # position


def demo_number():
    n = 2181200000
    d = 231456.75624
    a = -1234.50
    b = -343.25
    print("{}".format(n))
    print("{:,}".format(n))
    print("-" * 20)
    print("{}".format(d))
    print("{:.2f}".format(d))
    print("-" * 50)
    print("{:,.2f}".format(d))
    print("{:,.2f}".format(a))
    print("{:,.2f}".format(b))
    print("-" * 50)
    print("{:20,.2f}".format(d))    # align right
    print("{:=20,.2f}".format(a))
    print("{:20,.2f}".format(b))


demo_number()
