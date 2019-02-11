# this program calculates retail prices

mark_up = 2.5  # the mark-up percentage
another = "y"  # variable to control the loop

# process one or more item
while another == "y" or another == "Y":
    # get the item's wholesale cost
    wholesale = float(input("Enter the item's wholesale cost: "))
    
    # validate the wholesale cost
    while wholesale < 0:
        print("ERROR: the cost cannot be negative.")
        wholesale = float(input("Enter the correct wholesale cost: "))
        
    # calculate the retail price
    retail = wholesale * mark_up
    
    # display the retail price
    print("Retail price: $", format(retail, ",.2f"))
    
    # do this again?
    another  = input("Do you have another item?" +\
                     "(Enter y for yes): ")