# number analysis program

def main():
    numbers_list = get_numbers()
    total = get_total(numbers_list)
    
    # display the lowest number in the list
    lowest = min(numbers_list)
    print("The lowest number entered is", lowest)
    
    # display the highest
    highest = max(numbers_list)
    print("The highest number entered is", highest)
    
    # display the total of the numbers in the list
    print("The total of the numbers in the list is", total)
    
    # display the average of numbers in the list
    average = total / len(numbers_list)
    print("The average of the numbers in the list is", average)
    
def get_numbers():
    # create an empty list
    numbers = []
    
    # create a variable to hold the count of items entered
    index = 0
    
    # ask the user to enter a series of 20 numbers and 
    # append them into a list and return the list
    for index in range(20):
        print("Enter number #", index+1, ": ", sep="", end="")
        value = int(input())
        numbers.append(value)
    return numbers
    
def get_total(numbers_list):
    # create an accumulator
    total = 0.0
    
    # calculate the total of the elements in the list
    for num in numbers_list:
        total += num
        
    return total
    
# call the main function
main()
    