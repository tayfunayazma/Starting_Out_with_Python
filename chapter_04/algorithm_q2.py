# create a variable to control the loop
keep_going = "y"

# calculate the sum of numbers
while keep_going == "y":
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter another number: "))
    total = number1 + number2
    
    # display the sum of numbers
    print("The total is: ", total)
    
    # see if the user wants to perform the operation again
    keep_going = input("Do you wish to perform the operation again? if yes, enter y: ")