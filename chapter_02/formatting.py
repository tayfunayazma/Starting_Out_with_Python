# this program demonsrates how a floating-point number can be formatted
amount_due = 50000.0
monthly_payment = amount_due / 12
print("The monthly payment is ", format(monthly_payment, '.2f'))

# format functions returns the value as a string
print("The monthly payment is ",float(format(monthly_payment, '.2f')))

# Escape character (\) means that lines continues
print("The monthly payment is ", \
     format(monthly_payment, '.2f'))

# inserting comma separators
print("The monthly payment is: ", format(monthly_payment, ',.2f'))