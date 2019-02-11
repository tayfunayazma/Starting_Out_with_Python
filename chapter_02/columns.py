# this program displays the following floating-point numbers in a column with their decimal points aligned
num1 = 127.899
num2 = 3465.148
num3 = 3.776
num4 = 264.821
num5 = 88.081
num6 = 799.999

# display each number in a field of 7 spaces with 2 decimal places
print(format(num1, "7.2f"))
print(format(num2, "7.2f"))
print(format(num3, "7.2f"))
print(format(num4, "7.2f"))
print(format(num5, "7.2f"))
print(format(num6, "7.2f"))

# formating a floating number as a percentage
print(format(0.5, '%'))
print(format(0.5, '.0%'))