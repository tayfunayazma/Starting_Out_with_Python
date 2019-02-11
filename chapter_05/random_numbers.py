# this program displays a random number
# in the range of 1 through 100

import random

def main():
    # get a random number
    number = random.randint(1,100)
    # display the number
    print("The number is", number)
    
# call the main function
main()