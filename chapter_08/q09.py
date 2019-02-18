# vowels and consonants

def main():
    user_string = input("Enter a string: ")
    
    vowels, consonants = vowel_consonant_num(user_string)
    print("The number of vowels is", vowels, "and the number of consonants", consonants)
    
def vowel_consonant_num(user_string):
    # create a list of vowels
    vowel_list = ["a", "e", "i", "o", "u"]
    
    # set accumulators
    vowels = 0
    consonants = 0
    
    # read every character from the string
    for ch in user_string:
        # check if it is alphabetic character
        if ch.isalpha():
            # decide whether it is vowel or consonant
                if ch in vowel_list:
                    vowels += 1
                else:
                    consonants += 1
                    
    return vowels, consonants
    
    
# call the main function
main()
    