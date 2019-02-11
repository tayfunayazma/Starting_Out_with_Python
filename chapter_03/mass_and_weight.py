# mass and weight example

# ask the user to enter an object's mass
mass = float(input("Enter an object's mass: "))

# calculate its weight
weight = mass * 9.8

# decision-structure
if weight > 500:
    print("It it too heavy")
elif weight < 100:
    print("It is too light")
else:
    print("Error")