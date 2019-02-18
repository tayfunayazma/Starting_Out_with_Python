# character analysis

def main():
    # open the file
    infile = open("text.txt", "r")
    
    # read the content
    lines = infile.readlines()
    
    # close the file
    infile.close()
    
    #print(lines)
    
    # set accumulators
    num_uppercase = 0
    num_lowercase = 0
    num_digits = 0
    num_whitespace = 0
    
    # for each element in the list 
    for line in lines:
        # for each character in each sentence
        for ch in line:
            if ch.isupper():
                num_uppercase += 1
            if ch.islower():
                num_lowercase += 1
            if ch.isdigit():
                num_digits += 1
            if ch.isspace():
                num_whitespace += 1
                
        
    print("The number of uppercase letters in the file is", num_uppercase)
    print("The number of lowercase letters in the file is", num_lowercase)
    print("The number of digits in the file is", num_digits)
    print("The number of whitespace characters in the file is", num_whitespace)
    
# call the main function
main()
        
    