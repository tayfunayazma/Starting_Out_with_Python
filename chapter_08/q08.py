# sentence capitalizer

def main():
    # ask the user to enter a string
    user_string = input("Enter several sentences: ")
    
    get_string(user_string)
    
def get_string(user_string):
    # convert string to a list
    user_string_list = user_string.split(".")
    print(user_string_list)
    
    # capitalize each elements first character and print
    for i in user_string_list:
        print(i.strip().capitalize() + ". ", end="")
         
# call the main function
main()
    
    