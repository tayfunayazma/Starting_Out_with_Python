# this program display the line numbers

def main():
    # ask the user to enter a file name
    filename = input("Enter the file name: ")
    
    # open the file
    infile = open(filename, "r")
    
    # initialize a variable to keep count of the lines
    count = 0
    
    # read the contents from the file
    for  line in infile:
        line = float(line)
        # add 1 to the count variable
        count += 1
        print("Line #", count, ": ", line, sep="")
        
    # close the file
    infile.close()
    
# call the main function
main()