# this program displays the numbers of names
# that are stored in names.txt file

def main():
    try:    
        # initialize an accumulator
        total = 0.0
        
        # open the file
        infile = open("names.txt", "r")
        
        # read the lines and count the number of names in the file
        for line in infile:
            
            # add 1 to the total
            total += 1
        
        # close the file
        infile.close()
        
        # display the number of names
        print("The total number of names in the file is", total)
        
    except Exception as err:
        print(err)
    
# call the main function
main()