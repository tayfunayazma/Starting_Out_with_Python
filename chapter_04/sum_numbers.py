# this program calculates the sum of a series of numbers entered by the year

maxim = 5     # the maximum number

# initialize an accumulator variable
total = 0.0

# explain what we are doing
print("This program calculates the sum of")
print(maxim, "numbers you will enter.")

# get the numbers and accumulate them
for counter in range(maxim):
    number = int(input("Enter a number: "))
    total = total + number

# display the total of the numbers
print("The total is", total)