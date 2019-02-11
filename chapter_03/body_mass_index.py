# body mass index

# ask the user to enter his/her weight and height
weight1 = float(input("Enter your weight in pounds: "))
height1 = float(input("Enter your height in inches: "))

# calculate the user's BMI
bmi = weight1*703/height1**2

# display the user's BMI and if he/she has optimal weight, is under-weight, or is overweight
if bmi >= 18.5 and bmi <= 25:
    print("Your BMI is", format(bmi, ",.1f"))
    print("You weight is optimal")
elif bmi > 0 and bmi < 18.5:
    print("Your BMI is", format(bmi, ",.1f"))
    print("You are under-weight")
elif bmi > 25:
    print("Your BMI is", format(bmi, ",.1f"))
    print("You are overweight")
else:
    print("Error: Your entry is not correct")
