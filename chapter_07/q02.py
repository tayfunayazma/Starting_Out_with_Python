# lottery number generator

import random

def main():
    # create a list with 7 elements
    lottery_number = [0] * 7
    
    # generate random numbers for each of the elements in the list
    for i in range(7):
        lottery_number[i] = random.randint(0,9) 
    
    # display the lottery numbers    
    print("The lottery numbers are:", lottery_number)

# call the main function
main()    
    
    