#function Calculate BMI
def BmiCalculate(x,y):
    #calculate
    bmi = y / ((x * x) / 10000)
    #result to .1 point
    bmi = round(bmi, 1)
    return bmi

#input weight and Height
x = float(input("Enter your Height(cm.) : "))
y = float(input("Enter your Weight(kg.) : "))

#call function
bmi = BmiCalculate(x,y)

print("Your BMI : ",bmi)
#print('Your BMI : '+format(bmi,'.2f'))

#find description bmi
if bmi > 30 :
    print("You are Obese")
elif bmi > 25 :
    print("You are Overweight")
elif bmi > 18.5 :
    print("You are Smart")
elif bmi > 16 :
    print("You are Thinness")
else:
    print("You are Severe Thinness")