# this program read the random numbers stored in random_numbers.txt

def main():
    try:    
        # initialize an accumulator
        total = 0.0
        
        # initialize a variable to count the lines
        count = 0
        
        # open the file in reading mode
        infile = open("random_numbers.txt", "r")
        
        # read the lines from the file
        for line in infile:
            line = float(line)
            print(line)
            
            # add 1 to the count variable
            count += 1
            
            # calculate the sum of the random numbers
            total += line
            
        # close the file
        infile.close()
        print("The total of numbers is", total)
        print("There are", count, "random numbers read from the file.")
    
    except ValueError:
        print("ERROR: The file has no numeric data")
        
# call the main function
main()