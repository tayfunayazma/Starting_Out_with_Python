# this program generates 100 random number and keeps the count of
# how many of those random numbers are even and how many of them are odd

import random

def main():
    
    # set accumulators for odd and even numbers
    total_odd_numbers = 0
    total_even_numbers = 0 
    
    for n in range (100):
        number = get_random()
        if number % 2 == 0:
            total_even_numbers += 1
        else:
            total_odd_numbers += 1
    print("There are", total_even_numbers, "even numbers and", total_odd_numbers, "odd numbers.")

# generate 100 random numbers    
def get_random():
    for i in range(100):
        number = random.randint(1,100)
        print(number)
        return number
    
# call the main function    
main()