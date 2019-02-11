# this program adds coffee inventory records to the coffee.txt file

def main():
    # create a variable to control the loop
    another = "y"
    
    # open the coffee.txt file in append mode
    coffee_file = open("coffee.txt", "a")
    
    # add records to the file
    while another == "y" or another == "Y":
        # get the coffee record data
        print("Enter the following coffee data:")
        descr = input("Description: ")
        qty = int(input("Quantity (in pounds): "))
        
        # append the data to the file 
        coffee_file.write(descr + "\n")
        coffee_file.write(str(qty) + "\n")
        
        # determine whether the user want to add another record to the file
        print("Do you want to add another records? ")
        another = input("Y = yes, anything else = no: ")
        
    # close the file
    coffee_file.close()
    print("Data appended to coffee.txt.")
    
# call the main function
main()