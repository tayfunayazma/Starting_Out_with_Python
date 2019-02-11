# variables to represent the base hours and
# the overtime multiplier

base_hours = 40     #base hours per week
ot_multiplier = 1.5 #overtime multiplier

# get the hours worked and the hourly pay rate
hours = float(input("Enter the number of hours worked: "))
pay_rate = float(input("Enter the hourly pay rate: "))

# calculate and display the gross pay
if hours > base_hours:
    # calculate the gross pay with overtime
    # first, get the number of overtime hours worked
    overtime_hours = hours - base_hours
    
    # calculate the amount of overtime pay
    overtime_pay = overtime_hours * pay_rate * ot_multiplier
    
    # calculate the gross pay
    gross_pay = base_hours * pay_rate + overtime_pay
    
else:
    # calculate the gross pay without overtime
    gross_pay = hours * pay_rate
    
# display the gross pay
print("The gross pay is $", format(gross_pay, ',.2f'), sep="")