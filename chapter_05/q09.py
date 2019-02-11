# this program calculates monthly sales tax

# set the state and county sales taxes as constant
STATE_SALES_TAX = 0.05
COUNTY_SALES_TAX = 0.025

def main():
    sale_amount = float(input("Enter the amount of sale for this month: "))
    print()
    county_tax = county_sale_tax(sale_amount)
    state_tax = state_sale_tax(sale_amount)
    total_tax(county_tax, state_tax)

# calculations of county and state sales taxes and the total sales tax    
def county_sale_tax(sale):
    county_sale_tax = sale * COUNTY_SALES_TAX
    print("The amount of county sales tax is $", format(county_sale_tax, ",.2f"), sep="")
    return county_sale_tax
    
def state_sale_tax(sale):
    state_sale_tax = sale * STATE_SALES_TAX
    print("The amount of state sales tax is $", format(state_sale_tax, ",.2f"), sep="")
    return state_sale_tax
    
def total_tax(county, state):
    tax = county + state
    print("The total sales tax is $", format(tax, ",.2f"), sep="")
    
# call the main function       
main()