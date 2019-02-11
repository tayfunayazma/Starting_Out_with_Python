# how much insurance?

def main():
    replacement_cost = float(input("Enter the replacement cost of the building: "))
    insurance(replacement_cost)

# calculate the insurance cost    
def insurance(cost):
    min_insurance = cost * 0.80
    print("The minimum insurance cost you need pay is $", format(min_insurance, ",.2f"), sep="")

# call the main function    
main()