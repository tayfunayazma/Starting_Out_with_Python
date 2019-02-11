# this program display the average rainfall for a number of years

# ask user to enter the number of years
num_years = int(input("Enter the number of years: "))

# set the accumulator
total_rainfall = 0.0

for num_years in range(num_years):
    for months in range(1, 13):
        print("Enter the amount of rainfall in inches for year", \
              num_years+1, "month", months, end="")
        rainfall_inch = float(input(": "))
        total_rainfall += rainfall_inch
        months += 1
    # display the total and average rainfall   
    print("The total rainfall for", num_years+1, "years is", total_rainfall, "inches")
    average = total_rainfall / 12
    print("The average rainfall for", num_years+1, "years is", average, "inches")
    print()