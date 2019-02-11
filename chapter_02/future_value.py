# get the desired future value
future_value = float(input("Enter the desired future value: "))

# get the annual interest rate
rate = float(input("Enter the annual interest rate: "))

# get the number of years that the money will sit in the account
years = int(input("Enter the number of years the money will grow: "))

# calculate the amount that will have to be deposited
present_value = future_value / (1 + rate) ** years

# display the amount needed to deposit
print("You will need to deposit this amount: ", present_value)

# displaying the outputs on the same line
print("One", end=" ")
print("Two", end=" ")
print("Three")