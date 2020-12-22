def leap_year_ad(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def leap_year_be(year):
    if year % 4 == 3:
        return True
    else:
        return False


# print(leap_year)
print(leap_year_ad(2020))
print(leap_year_be(2563))

