# file head display

def main():
    # ask the user to enter the file name
    filename = input("Enter the file name: ")
    
    # open the file
    infile = open(filename, "r")
    
    # read the contents
    for i in range(5):
        line = infile.readline()
        
        # strip \n from the file
        line = line.rstrip("\n")
        
        # display the lines
        print(line)
        
    # close the file
    infile.close()
    
# call the main function
main()