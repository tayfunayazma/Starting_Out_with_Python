# Golf score

def main():
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
        
    # close the file
    outfile.close()
    print("Data written to golf.txt.")
    
# call the main function
main()