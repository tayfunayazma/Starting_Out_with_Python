# this program calculates gross pay

def main():
    try:
        # get the number of hours worked
        hours = int(input("How many hours did you work? "))
        
        # get the hourly pay rate
        pay_rate = float(input("Enter your hourly pay rate: "))
        
        # calculate the gross pay
        gross_pay = hours * pay_rate
        
        # display the gross pay
        print("Gross pay: $", format(gross_pay, ",.2f"), sep="")
        
    except ValueError as err:
        print(err)
        
# call the main function
main()