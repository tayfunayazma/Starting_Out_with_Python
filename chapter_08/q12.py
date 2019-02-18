# pig Latin

def main():
    # ask the user to enter a sentence to covert it to Latin
    user_string = input("Enter a sentence: ")
    user_string = user_string.upper()
    
    # split each word by space
    word_list = user_string.split()
    print(word_list)
    # process each for one by one
    for word in word_list:
        # concatenate strings using index
        print(word[1:], word[0], "AY ", sep="", end="")
        
# call the main function
main()