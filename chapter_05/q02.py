# sales tax programming refactoring

# constants
STATE_SALES_TAX = 0.05
COUNTY_SALES_TAX = 0.025


def main():
    purchase_price = float(input("Enter the amount of purchase: "))
    state_taxes(purchase_price)
    county_taxes(purchase_price)
    sales_taxes = total_sales_taxes(purchase_price)
    print()
    total(purchase_price, sales_taxes)

# the calculations of state sales taxes    
def state_taxes(price):
    state_taxes = price * STATE_SALES_TAX
    print("The total state sales tax is $:", format(state_taxes, ",.2f"), sep="")
    return state_taxes

# the calculations of county sales taxes
def county_taxes(price):
    county_taxes = price * COUNTY_SALES_TAX
    print("The total county sales tax is $:", format(county_taxes, ",.2f"), sep="")
    return county_taxes

# the total sales taxes    
def total_sales_taxes(price):
    tax = price * (STATE_SALES_TAX + COUNTY_SALES_TAX)
    print("The total sales tax is $", format(tax, ",.2f"), sep="")
    return tax

# the total amount of purchase including sales price and taxes
def total(price, sales_taxes):
    total_sale = price + sales_taxes
    print("Total of the sale is $", format(total_sale, ",.2f"), sep="")
    return total_sale

# call the main function
main()