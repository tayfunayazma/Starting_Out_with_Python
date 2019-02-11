# this program gets an item's original price and calculates its sale price, with 20% discount
# get the item's original price
original_price = float(input("Enter the item's original price: "))

# calculate the amount of the discount
discount = original_price * 0.2

# calculate the sale price
sale_price = original_price - discount

# display the sale price
print("The sale price is ", sale_price)