# word separator

def main():
    print("Example: StopAndSmellTheRoses")
    user_string = input("Enter a string like above: ")
    
    separator(user_string)
    
def separator(string):
    # seprate it by uppercase character
    # first letter would be capital
    print(string[0].upper(), end="")
    
    index = 1   # the first letter already capitalized so start from the second element
    
    while index < len(string):
        if string[index].isupper():
            print(" ", end="")
            print(string[index].lower(), end="")
        else:
            print(string[index].lower(), end="")
            
        index += 1
        
    print(".")
    
# call the main function
main()