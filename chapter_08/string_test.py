# this program demonstrates several strings testing methods

def main():
    # get a string from the user
    user_string = input("Enter a string: ")
    
    print("This is what I found about that strings:")
    
    # test the string
    if user_string.isalnum():
        print("The string is alphanumeric.")
    if user_string.isdigit():
        print("The string contains only digits.")
    if user_string.isalpha():
        print("The string contains only alphabetical characters.")
    if user_string.isspace():
        print("The string contains only whitespace characters.")
    if user_string.islower():
        print("The letters in the string are all lowercase.")
    if user_string.isupper():
        print("The letters in the string are all uppercase.")
        
# call the main function
main() 