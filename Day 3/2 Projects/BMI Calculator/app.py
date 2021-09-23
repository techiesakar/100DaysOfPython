# BMI calculator
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
BMI = int(weight/height**2)
print("weight : ", weight)
print("height : ", height)
print("BMI : ", BMI)

if BMI > 35:
    print("You are clinically obese")
elif 30 < BMI < 35:
    print("You are obese")
elif 25 < BMI < 30:
    print("You are overweight")
elif 18.5 < BMI < 25:
    print("You have normal weight")
else:
    print("You are under weight")
