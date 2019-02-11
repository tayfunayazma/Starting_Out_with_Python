# this program demonsrates how a floating-point number is displayed with no formatting
amount_due = 5000.0
monthly_payment = amount_due/12.0
print("The monthly payment is ", monthly_payment)

# formating displayed number
print("The monthly payment is ", format(monthly_payment, ".2f"))