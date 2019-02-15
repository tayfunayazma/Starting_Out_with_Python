# total sales

NUM_DAYS = 7

def main():
    # create a list to hold sales for each day
    sales = [0] * NUM_DAYS
    
    # create an index to hold an index
    index = 0
    
    # create an accumulator
    total = 0
    
    print("Enter the sales for each day.")
    
    while index < NUM_DAYS:
        print("Day #", index+1, ": ", sep="", end="")
        sales[index] = float(input())
        index += 1
        
    print("Here are the values you entered")
    for value in sales:
        print(value)
        
        total += value
        
    # display the total sales
    print()
    print("The total sales for the week is", total)

# call the main function
main()
    
    