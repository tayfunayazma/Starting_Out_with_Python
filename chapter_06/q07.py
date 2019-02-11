# this program writes random numbers from 1 through 500 in a file

import random

def main():
    # ask the user to enter the number of random numbers to be generated
    num_random_numbers = int(input("How many random numbers do you want to generate? "))
    
    # open a file
    outfile = open("random_numbers.txt", "w")
    
    # generate random numbers
    for i in range(num_random_numbers):
        random_number = random.randint(1,500)
        print(random_number)
    
        # write the random numbers to the file
        outfile.write(str(random_number) + "\n")
    
    # close the file
    outfile.close()
    print("Random numbers written to the random_numbers.txt file.")

# call the main function    
main()