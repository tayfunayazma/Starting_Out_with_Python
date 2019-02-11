# this program compares two strings
# get a password from the user
password = input("Enter the password: ")

# determine whether the correct password was entered
if password == "prospero":
    print("Password accepted.")
else:
    print("Sorry, that is the wrong password.")
    
# string comparisons are case sensitive