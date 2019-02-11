# this program demonstrate an infinite loop
# create a variable to control the loop
keep_going = "y"

# warning infinite loop
while keep_going == "y":
    # get sale's person sales and commission rate
    sales = float(input("Enter the amount of sales: "))
    comm_rate = float(input("Enter the commission rate: "))
    
    #calculate the commission
    commission = sales * comm_rate
    
    # display the commission
    print("The commission is $", \
          format(commission, ",.2f"), sep="")