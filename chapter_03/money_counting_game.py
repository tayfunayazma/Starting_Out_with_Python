# money counting game

# ask the user to enter the number of pennies, nickels, dimes, and quarters. 
pennies = int(input("Enter the number of pennies: "))
nickels = int(input("Enter the number of nickels: "))
dimes = int(input("Enter the number of dimes: "))
quarters = int(input("Enter the number of quarters: "))

# determine if the total value of the coins is equal to one dollar
if (pennies + nickels*5 + dimes*10 + quarters*25) == 100:
    print("Congratulations, you have one dollar")
elif (pennies + nickels*5 + dimes*10 + quarters*25) > 100:
    print("Sorry, you have more than one dollar")
else:
    print("Sorry, you have less than one dollar")