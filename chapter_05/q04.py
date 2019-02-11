# automobile costs

def main():
    loan_payment = loan_payment_cost()
    insurance = insurance_cost()
    gas = gas_cost()
    oil = oil_cost()
    tires = tires_cost()
    maintenance = maintenance_cost()
    total_payment = total(loan_payment, insurance, gas, oil, tires, maintenance)
    total_annual_cost = total_payment * 12
    print("The total monthly cost of these expenses is $", format(total_payment, ",.2f"), sep="")
    print("The total annual cost of these expenses is $", format(total_annual_cost, ",.2f"), sep="")

# ask the user to enter the monthly expenses for each item below and return the value   
def loan_payment_cost():
    loan_payment = float(input("Enter the loan payment of your car: "))
    return loan_payment
    
def insurance_cost():
    insurance = float(input("Enter the monthly insurance payment: "))
    return insurance
    
def gas_cost():
    gas = float(input("Enter the monthly payment for gas: "))
    return gas

def oil_cost():
    oil = float(input("Enter the monthly payment for oil: "))
    return oil
        
def tires_cost():
    tires = float(input("Enter the monthly payment for tires: "))
    return tires

def maintenance_cost():
    maintenance = float(input("Enter the monthly maintenance cost: "))
    return maintenance

def total(loan_payment, insurance, gas, oil, tires, maintenance):
    total = loan_payment + insurance + gas + oil + tires + maintenance
    return total

# call the main function
main()
    
    
    