# rainfall statistics

def main():
    rainfall = get_rainfall()
    total = total_rainfall(rainfall)
    print("The total rainfall for the year is", total)
    average = total / len(rainfall)
    print("The average monthly rainfall is", format(average, ",.2f"))
    lowest = min(rainfall)
    print("The lowest amount of monthly rainfall is", lowest)
    highest = max(rainfall)
    print("The highest amount of monthly rainfall is", highest)
    
def get_rainfall():
    # create a list
    rainfall = []
    
    # create an index variable
    index = 0
    
    # ask the user to enter the amount for each month and
    # append the value to the list
    for index in range(12):
        print("Enter the total rainfall for the month #", index+1, ": ", sep="", end="")
        value = float(input())
        rainfall.append(value)
    
    return rainfall

def total_rainfall(rainfall):
    # create an accumulator
    total = 0.0
    
    # calculate the total rainfall for the year
    for num in rainfall:
        total += num
        
    return total

# call the main function
main()
