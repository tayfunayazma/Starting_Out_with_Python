# Morse code converter

def main():
    # ask the user to enter a string
    user_string = input("Enter a string: ")
    
    # convert all strings to uppercase
    user_string = user_string.upper()
    
    # split string into character list
    user_string_list = list(user_string)
    print(user_string_list)
    print()
    
    # create list of character and morse in the same order
    character = [" ", ",", ".", "?", "0", "1", "2", "3", "4", "5", "6", "7", "8",
                 "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                 "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    
    morse = [" ", "--..--", ".-.-.-", "..--..", "-----", ".----", "..---", "...--", "....-", ".....",
             "-....", "--...", "---..", "----.", ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
             "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", 
             "...-", ".--", "-..-", "-.-", "--.."]
    
    print("The string converted to morse:")
    
    # get the index code of user string in the character list
    index = 0
    while index < len(user_string_list):
        # find the index in the morse list 
        position = character.index(user_string_list[index])
        print(morse[position], end=" ")
        index += 1
        
# call the main function
main()
        