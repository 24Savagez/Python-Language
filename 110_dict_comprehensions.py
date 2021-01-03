import datetime


def demo1():
    t = [("sun", "red"), ("mon", "yellow"), ("tue", "pink"), ("wed", "green"),
         ("thu", "orange"), ("fri", "blue"), ("sat", "purple")]
    d = {}
    for k, v in t:
        d[k] = v
    print(d)
    # dict comprehensions
    d1 = {k.capitalize(): v for k, v in t}
    print(d1)

    today = datetime.datetime.now()
    print(today.strftime("%a"))
    weekday = today.strftime("%a")
    weekcolor = d1[weekday]
    print(weekday, weekcolor)


def demo2():
    weekdays = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]
    weekcolor = ["red", "yellow", "pink", "green", "orange", "blue", "purple"]
    # generators
    t = zip(weekdays, weekcolor)
    # dict comprehensions
    d1 = {k.capitalize(): v for k, v in t}
    print(d1)


# demo1()
demo2()
