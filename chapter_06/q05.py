# this program reads the contents in numbers.txt file
# and display the sum of the number in the file

def main():
    try:    
        # open the file
        infile = open("numbers.txt", "r")
        
        # initialize an accumulator
        total = 0.0
        
        # read the contents of the file
        for line in infile:
            line = float(line)
            print(line)
            
            # calculate the sum of the numbers
            total += line
        # close the file
        infile.close()
        
        # display the sum 
        print("The sum of the numbers in file is", total)
    
    # this exception is for non-numeric contents    
    except ValueError:
        print("The file has non-numeric contents")

# call the main function
main()        