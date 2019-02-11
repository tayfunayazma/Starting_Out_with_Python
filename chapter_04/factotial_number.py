number = int(input("Enter a nonnegative number: "))
factorial = 1

# validate if the user enters a nonnegative number
while number < 0:
    number = int(input("Please enter a nonnegative number: "))

# calculate the factorial
for i in range(1, number+1):
    factorial *= i

# display the factorial of the number entered
print()
print("Factorial of", number, "is", factorial)