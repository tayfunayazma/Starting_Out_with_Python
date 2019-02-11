# this program calculates the future value of money in a bank account

def main():
    present_value = float(input("Enter the account's present value: "))
    interest_rate = float(input("Enter the monthly interest rate: "))
    num_months = int(input("Enter the number of months money will be" + \
    "left in the account: "))
    future_value = get_future_value(present_value, interest_rate, num_months)
    print("The amount that you will have after ", num_months, " month is $", \
          format(future_value, ",.2f"), sep="")

# calculations to get the future value
def get_future_value(p, i, t):
    return p * (1 + i)**t


# call the main function
main()
    