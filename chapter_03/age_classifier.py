# age classifier example

# ask the user to enter his/her age
age = int(input("Enter your age: "))

# determine whether the user is a/an infant, child, teenager, or adult
if age <= 1:
    print("Infant")
elif age > 1 and age < 13:
    print("Child")
elif age >= 13 and age < 20:
    print("Teenager")
else:
    print("Adult")