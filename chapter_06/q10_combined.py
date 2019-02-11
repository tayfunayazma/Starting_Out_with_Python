# golf score

def main():
    try: 
        write_program()
        read_program()
        
    except Exception as err:
        print(err)
    
def write_program():
    # create variable to control the loop
    another = "y"
    
    # open the golf.txt file
    outfile = open("golf.txt", "w")
    
    # add records to the file
    while another == "y" or another == "Y":
        # get the player's name
        print("Enter the following player's data:")
        name = input("Enter the player's name: ")
        score = int(input("Enter the player's golf score: "))
        
        # write the data to the file
        outfile.write(name + "\n")
        outfile.write(str(score) + "\n")
        
        # determine whether the user wants to add another record to the file
        print()
        print("Do you want to add another record?")
        another = input("Y = yes, anything else = no: ")
        print()
        
    # close the file
    outfile.close()
    print("Data written to golf.txt.")
    print()
    
def read_program():
    # open the golf.txt file
    infile = open("golf.txt", "r")
    
    # read the first record's name field
    name = infile.readline()
    
    # print the headings
    print("Name\t\t\tScore")
    print("------------------------------")
    
    # read the rest of the file
    while name != "":
        # read the score field
        score = float(infile.readline())
        
        # strip the \n from the name
        name = name.rstrip("\n")
        
        # display the record
        print(name, "\t\t", score)
        
        # read the next name
        name = infile.readline()
        
    # close the file
    infile.close()
    
# call the main function
main()