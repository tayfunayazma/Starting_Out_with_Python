item1 = float(input("Enter the price of the item: "))
state_sales_tax = 0.05
country_sales_tax = 0.025
total_sales_tax = item1 * (state_sales_tax + country_sales_tax)
print(item1)
print(state_sales_tax)
print(country_sales_tax)
print(format(total_sales_tax, '.2f'))
print(item1 + total_sales_tax)