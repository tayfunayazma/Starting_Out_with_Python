# ask the user to enter a number
number = int(input("Enter a positive number: "))

# validate the number to be positive
while number < 0:
    print("ERROR: ", end="")
    number = int(input("Enter a positive number: "))