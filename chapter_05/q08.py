# this program estimates the cost of a paint job

# constant for labor hour
LABOR_HOUR_CHARGE = 35

def main():
    square_feet = float(input("Enter the square feet of wall space to be painted: "))
    price_pergallon = float(input("Enter the price of the paint per gallon: "))
    print()
    required_gallons = num_gallons(square_feet)
    required_hours = hour_labor(square_feet)
    cost = cost_paint(price_pergallon, required_gallons)
    labor = labor_charge(required_hours)
    total_cost(cost, labor)    
    
def num_gallons(square_feet):
    required_gallons = square_feet / 112
    print("The number of gallons paint required is", required_gallons)
    return required_gallons
    
def hour_labor(square_feet):
    required_hours = square_feet / 112
    print("The number of labor hours required is", required_hours)
    return required_hours

def cost_paint(price_pergallon, required_gallons):
    cost_paint = price_pergallon * required_gallons
    print("The cost of the paint is $", format(cost_paint, ",.2f"), sep="")
    return cost_paint
    
def labor_charge(required_hours):
    cost_labor = required_hours * LABOR_HOUR_CHARGE
    print("The labor charges is $", format(cost_labor, ",.2f"), sep="")
    return cost_labor
    
def total_cost(paint, labor):
    total_cost = paint + labor
    print("The total cost of the paint job is $", format(total_cost, ",.2f"), sep="")

# call the main function    
main()
    