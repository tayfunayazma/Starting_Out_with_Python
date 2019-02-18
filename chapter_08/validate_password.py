# this program gets a password from the user and validate it

import login1

def main():
    # get a password from the user
    password = input("Enter your password: ")
    
    # validate the password
    while not login1.valid_password(password):
        print("That password is not valid")
        password = input("Enter your password: ")
        
    print("That is a valid password.")

# call the main function
main()