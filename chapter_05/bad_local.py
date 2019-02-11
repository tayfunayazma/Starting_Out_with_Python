# definition of the main function (Corrected)
def main():
    get_name()
        # this causes an error!
    
# definition of the get_name function
def get_name():
    name = input("Enter your name: ")
    print("Hello", name)
    
# call the main function
main()