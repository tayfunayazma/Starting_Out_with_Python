# this program display the contents of numbers.txt file

def main():
    # open the file named numbers.txt
    infile = open("numbers.txt", "r")
    
    # read the file
    for line in infile:
        # strip the \n from the lines
        line = float(line)
        #line = line.rstrip("\n")
        
        print(line)
        
    # close the file
    infile.close()
    
# call the main function
main()