# if-elif-else statement
# get a test score from the user
score = int(input("Enter a test score: "))

# determine the grade letter using if-elif-else statement
if score >= 90:
    print("Your grade is A")
elif score >= 80:
    print("Your grade is B")
elif score >= 70:
    print("Your grade is C")
elif score >= 60:
    print("Your grade is D")
else:
    print("Your grade is F")