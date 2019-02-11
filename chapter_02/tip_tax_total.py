amount_meal = float(input("Enter the total amount of meal purchased: "))
tip = 0.18
sales_tax = 0.07
print(amount_meal)
print(tip)
print(sales_tax)
total = amount_meal + (amount_meal * tip) + (amount_meal * sales_tax)
print("Your total is $", format(total, ',.2f'), sep="")