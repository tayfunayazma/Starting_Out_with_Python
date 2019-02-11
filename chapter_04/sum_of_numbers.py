# ask the user to enter a positive number
number = int(input("Enter a positive number: "))

# set the sum 0
sum_num = 0.0

# continue until the user enters a negative number
while number >= 0:
    sum_num += number
    print("Enter a positive number to continue or" +\
          " a negative number to end", end="")
    number = int(input(": "))

# display the sum of the numbers entered    
print()
print("The sum of the numbers you entered is", sum_num)