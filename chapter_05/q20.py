# this program simulates random number guessing game

import random

def main():
    random_num = get_random_number()    # get the random number generated in get_random_number function
    user_num = int(input("Enter a random number from 1 through 100: "))
    total_guess = 1     # create an accumulator to see the number of guesses
    keep_going = 1      # create a variable to control the loop
    
    while keep_going == 1:
        if compare_numbers(user_num, random_num) == False:
            keep_going = 1
            user_num = int(input("Sorry. Enter a new number: "))
            total_guess += 1
        else:
            keep_going = 0
    print("You found the correct number after", total_guess, "guesses.")
        
    
def get_random_number():
    number = random.randint(1,100)
    print(number)
    return number
    
def compare_numbers(user_num, random_num):
    if user_num > random_num:
        print("Too high, try again")
        status = False
    elif user_num < random_num:
        print("Too low, try again")
        status = False
    else:
        print("Congratulations. You found the number", random_num)
        status = True
    return status
    
    
main()