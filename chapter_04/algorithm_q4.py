total = 0.0
for t in range(10):
    number = int(input("Enter a number: "))             # ask the user to enter a number
    total = total + number                              # calculate the total
print("The total is: ", format(total, ".0f"), sep="")   # display the sum of numbers entered