# ask the user to enter the starting number of organisms
num_organism = int(input("Enter starting number of organisms: "))

# ask the user to enter the average daily increase as a percentage and convert it for calculation
average_increase = float(input("Enter the average daily increase as a percentage: "))
average_increase = average_increase/100

# ask the user to enter the number of days to multiply
num_days = int(input("Enter the number of days to multiply: "))

print("Days\t\tPopulation")
print("---------------------------")

# display the table 
for num_days in range(1, num_days+1):
    print(num_days, "\t\t", format(num_organism, ",.1f"))
    num_organism = num_organism + (num_organism * average_increase)