# initials
def main():
    name = input("Enter your first, middle, and last name: ")
    names_list = name.split()
     
    for ch in names_list:
        print(ch[0], ". ", sep="", end="")
        
    # print(names_list[0][0], ". ", names_list[1][0], ". ", names_list[2][0], ". ", sep="")
    # the print function above gives error if the user enters only first and last name 
    
# call the main function
main()