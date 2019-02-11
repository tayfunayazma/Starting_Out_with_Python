# this program prompt the user to enter a file name
# and displays the contents (first five lines) from the file
# see a shorter version on q02_1.py

def main():
    # ask the user to enter the file name
    filename = input("Enter the file name: ")
    
    # open the file in reading mode
    infile = open(filename, "r")
    
    # read the first five lines
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    line4 = infile.readline()
    line5 = infile.readline()
    
    # strip the \n from the file
    line1 = line1.rstrip("\n")
    line2 = line2.rstrip("\n")
    line3 = line3.rstrip("\n")
    line4 = line4.rstrip("\n")
    line5 = line5.rstrip("\n")
    
    # display the contents
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)
    
    # close the file
    infile.close()
    
# call the main function
main() 
    