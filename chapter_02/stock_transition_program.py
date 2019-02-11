num_share = 2000
price_per_share = 40
commission = 2000 * 40 * 0.03
total_money = 2000 * 40
print(format(total_money, ",.2f"))
print(format(commission, ",.2f"))
total_sold = 2000 * 42.75
print(format(total_sold, ",.2f"))
commission_sold = total_sold * 0.03
print(format(commission_sold, ",.2f"))
profit = total_sold - total_money - commission - commission_sold
print("The profit is $", format(profit, ",.2f"), sep="")