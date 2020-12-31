def basic_method():
    fruits = {"mango", "banana"}
    fruits.add("apple")
    print(fruits)

    # fruits.add(("coconut", "papaya"))
    # print(fruits)

    fruits.update({"coconut", "papaya"})
    print(fruits)

    fruits = fruits | {"cherry", "strawberry", "kiwi", "mango"}
    print(fruits)

    fruits.remove("cherry")

    print(fruits)
    # fruits.remove("durian")
    fruits.discard("durian")

    print(fruits)
    if "mango" in fruits:
        print("great")

    fruits.clear()
    print(fruits)


def pass_skills(req_skills, applicant_skills):
    return req_skills <= applicant_skills  # rea_skills เป็น subset ของ applicant_skills


def pass_skills2(req_skills, applicant_skills):
    a = req_skills & applicant_skills  # rea_skills เป็น intersect ของ applicant_skills
    if len(a) >= 2:
        return True
    else:
        return False


# basic_method()
req = {"Python", "R", "Java"}
applicant = {"Python", "Jalia", "Css", "Html"}
print(pass_skills(req, applicant))
print(pass_skills2(req, applicant))


