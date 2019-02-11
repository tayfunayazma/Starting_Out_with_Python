# this program simulates the rolling of dice
import random

# constant for the minimum and maximum random number
MIN = 1
MAX = 6

def main():
    # create a variable to control the loop
    again = "y"
    
    # simulating rolling dice
    while again == "y" or again == "Y":
        print("Rolling the dice ...")
        print("Their values are: ")
        #print(random.randint(MIN, MAX)) 
        #print(random.randint(MIN, MAX))
        for count in range(2):              # this is an alternative to the above
            print(random.randint(MIN, MAX))
        # Do another roll of the dice?
        again = input("Roll them again? (y = yes): ")
        
# call the main function
main()
    