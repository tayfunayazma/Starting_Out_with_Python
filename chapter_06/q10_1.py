def main():
    # open the golf.txt file
    infile = open("golf.txt", "r")
    
    # read the first record's name field
    name = infile.readline()
    
    # print the headings
    print("Name\t\tScore")
    print("---------------------")
    
    # read the rest of the file
    while name != "":
        # read the score field
        score = float(infile.readline())
        
        # strip the \n from the name
        name = name.rstrip("\n")
        
        # display the record
        print(name, "\t", score)
        
        # read the next name
        name = infile.readline()
        
    # close the file
    infile.close()
    
# call the main function
main()