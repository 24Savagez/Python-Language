try:
    score = int(input("Enter your Score : "))
    if score <= 100 and score >= 0:
        if score >= 80:
            print("Grade : A")
        elif score >= 75:
            print("Grade : B+")
        elif score >= 70:
            print("Grad : B")
        elif score >= 65:
            print("Grade : C+")
        elif score >= 60:
            print("Grade : C")
        elif score >= 55:
            print("Grade : D+")
        elif score >= 50:
            print("Grade : D")
        elif score >= 0:
            print("Gread : F")
    else:
        print("Invalid score")
except ValueError:
    print("Error,please try 0 - 100")

