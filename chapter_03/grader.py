# this program gets a numeric test score from
# the user and displays the corresponding letter grade

# get the test score from the user
score = int(input("Enter your test score: "))

# determine the grade
if score >= 90:
    print("Your grade is A")
else:
    if score >= 80:
        print("Your grade is B")
    else:
        if score >= 70:
            print("Your grade is C")
        else:
            if score >= 60:
                print("Your grade is D")
            else:
                print("Your grade is F")