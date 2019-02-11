# this program calculates budget for a month after subtracting expenses

# ask the user the budget for a month
budget = float(input("Enter the budget of this month: "))
total_expenses = 0.0

# set a varible to control the loop
keep_going = "y"

# set a variable for each expenses
counter = 0

while keep_going == "y" or keep_going =="Y":
    print("Enter the expenses", counter+1, end="")
    expenses = float(input(": "))
    total_expenses += expenses
    keep_going = input("Do you want to add another expense? if yes, enter 'y'")
    counter += 1
balance = budget - total_expenses

# display the budget and total expenses
print("Your budget is: ", budget)
print("Your total expenses is: ", total_expenses)

# display if the user over budget or under budget
if balance < 0:
    print("You are over budget in the amount of", balance)
else:
    print("You are under budget in the amount of", balance)