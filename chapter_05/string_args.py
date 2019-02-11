# this program demonstrates passing two string
# arguments to a function

def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your las name: ")
    print("Your name reversed is")
    reverse_name(first_name, last_name)
    
def reverse_name(first, last):
    print(last, first)
    
# call the main function
main()