# this program displays the pennies doubled everyday
# ask the user how many days he/she would like to work
num_days = int(input("Enter how many days you would like to work: "))

# print the headings
print("Days\tSalary")
print("--------------")

# set the accumulator
total = 0.0

# calculate the pennies for each day and convert to dollars
for num_days in range(1, num_days+1):
    salary = 2**(num_days-1)/100
    print(num_days, "\t", "$", format(salary, ",.2f"), sep="")
    total = total + salary
    
# display the total pay
print()    
print("Total pay is $", format(total, ",.2f"), sep="")
    
