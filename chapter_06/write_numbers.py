# this program demonstrates how numbers must be converted
# to the strings before they are written to a text file

def main():
    # open a file for writing
    outfile = open("numbers.txt", "w")
    
    # get three numbers from the user
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    num3 = int(input("Enter another number: "))
    
    # write the numbers to the file
    outfile.write(str(num1) + "\n")
    outfile.write(str(num2) + "\n")
    outfile.write(str(num3) + "\n")
    
    # close the file
    outfile.close()
    
    print("Data written to numbers.txt")
    
# call the main function
main()