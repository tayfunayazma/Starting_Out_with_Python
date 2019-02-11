item1 = float(input("Enter the price of the first item: "))
item2 = float(input("Enter the price of the second item: "))
item3 = float(input("Enter the price of the third item: "))
item4 = float(input("Enter the price of the fourth item: "))
item5 = float(input("Enter the price of the fifth item: "))
subtotal = item1 + item2 + item3 + item4 + item5
sales_tax = 0.07
total = subtotal + subtotal * sales_tax
print(subtotal)
print(sales_tax)
print(total)