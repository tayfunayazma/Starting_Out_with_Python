# ask the user to enter a number from 1 through 100
number = int(input("Enter a number in the range of 1 through 100: "))

# validate if the number is in range given
while number < 1 or number > 100:
    print("ERROR: ", end="")
    number = int(input("Enter a number again in the range of 1 through 100: "))
    