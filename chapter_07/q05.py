# charge account validation
def main():
    account_list = reading_list()
    determine_account(account_list)
    
def reading_list(): 
    # open the file for reading
    infile = open("charge_accounts.txt", "r")
    
    # read the content of the file into a list
    account_numbers = infile.readlines() 
    
    # close the file
    infile.close()
    
    # convert each element to an int
    index = 0
    while index < len(account_numbers):
        account_numbers[index] = int(account_numbers[index].rstrip("\n"))
        index += 1
        
    # print the contents of the list
    #print("The account numbers stored in the file are the following:")
    #print(account_numbers)
    
    return account_numbers 

def determine_account(account_list): 
    # get an account number to search for
    search = int(input("Enter a charge account number: "))
    
    # determine whether the number is valid
    if search in account_list:
        print("The charge account number is valid")
    else:
        print("The charge account number is NOT valid")
        
# call the main function
main()