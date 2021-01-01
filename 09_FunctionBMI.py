# function Calculate BMI
def bmi_calculate(height, weight):
    # calculate
    bmi_cal = weight / ((height * height) / 10000)
    # result to .1 point
    bmi_round = round(bmi_cal, 1)
    return bmi_round


# input weight and Height
height = float(input("Enter your Height(cm.) : "))
weight = float(input("Enter your Weight(kg.) : "))

# call function
bmi = bmi_calculate(height, weight)

print("Your BMI : ", bmi)
# print('Your BMI : '+format(bmi,'.2f'))

# find description bmi
if bmi > 30:
    print("You are Obese")
elif bmi > 25:
    print("You are Overweight")
elif bmi > 18.5:
    print("You are Smart")
elif bmi > 16:
    print("You are Thinness")
else:
    print("You are Severe Thinness")
