# Roulette wheel colors example

# ask the user to enter a pocket number
number = int(input("Enter a pocket number: "))

# determines whether the pocket is green, red or black.
if number == 0:
    print("Green")
elif number >= 1 and number <= 10:
    if number%2 == 0:
        print("Pocket", number, "is Black")
    else:
        print("Pocket", number, "is Red")
elif number >= 11 and number <= 18:
    if number%2 == 0:
        print("Pocket", number, "is Red")
    else:
        print("Pocket", number, "is Black")
elif number >= 19 and number <= 28:
    if number%2 == 0:
        print("Pocket", number, "is Black")
    else:
        print("Pocket", number, "is Red")
elif number >= 29 and number <= 36:
    if number%2 == 0:
        print("Pocket", number, "is Red")
    else:
        print("Pocket", number, "is Black")   
else:
    print("Error: the number is outside the range of 0 through 36")
                        