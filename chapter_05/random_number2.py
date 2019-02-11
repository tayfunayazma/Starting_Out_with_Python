# this program displays five random
# numbers in the range of 1 through 100.

import random

def main():
    for count in range(5):
        # get a number
        number = random.randint(1, 100)
        # display the number
        print(number)
        
# call the main function
main()

# alternative
print()
print(random.randint(1,100))
    