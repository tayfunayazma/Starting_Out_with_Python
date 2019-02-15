# name search

def main():
    # open the girlnames.txt file
    try: 
        girls_list = girls_name()
        boys_list = boys_name()
        search_name(girls_list, boys_list)
        
    except IOError:
        print("No such file or directory")
    
def girls_name(): 
    # open the girlnames.txt file   
    infile = open("girlnames.txt", "r")
    
    # read the contents of the file
    names = infile.readlines()
    
    # close the file
    infile.close()
    
    # strip the \n from the elements
    index = 0
    while index < len(names):
        names[index] = names[index].rstrip("\n")
        index += 1  
    return names

def boys_name():
    # open the file
    infile = open("boynames.txt", "r")
    
    # read the contents of the file
    names = infile.readlines()
    
    # close the file
    infile.close()
    
    # strip the \n from the elements
    index = 0
    while index < len(names):
        names[index] = names[index].rstrip("\n")
        index += 1
    return names

def search_name(girls_list, boys_list):
    # ask the user to enter a name to search for
    name = input("Enter a name: ")
    
    # determine whether the name is in the lists
    if name in girls_list or name in boys_list:
        print(name, "is among the most popular names.")
    else:
        print(name, "is NOT found among the most popular names.")  
     
# call the main function
main()
    
    