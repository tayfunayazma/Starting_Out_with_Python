# alphabetic telephone number translator

def main():
    tel_number = input("Enter a 10 character telephone number" +
                        "in the following format (XXX-XXX-XXXX): ")
    # create two list for alphabetic letters and numbers
    
    alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
             "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
    num = [2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]
    
    # convert to upper-case letters to lower-case
    tel_number = tel_number.lower()
    
    # go through each character in input
    index = 0
    while index < len(tel_number):
        # if it is alphabetical convert it to number, if not keep it
        if tel_number[index].isalpha():
            print(num[alpha.index(tel_number[index])], end="")
        else:
            print(tel_number[index], end="")
            
        index += 1
    
    
# call the main function
main()
    