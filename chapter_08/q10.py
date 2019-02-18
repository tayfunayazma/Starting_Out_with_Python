# most frequent character

def main():
    user_string=input("Enter a string: ")
    
    # create an empty list to store each character and
    # occurences list to store how many time it is repeated 
    # with same shared-index.
    char_list=[]
    occurences=[]
   
    # read every character in the string
    for ch in user_string.lower():
        # first make sure it is not whitespace or any other character than alphabet and number
        # simply use isalnum() for alphabetical and numerical characters.
        if ch.isalnum():
            # if it is not in the list append it to char_list
            if ch not in char_list:
                char_list.append(ch)
                # and place its first occurence
                occurences.append(1)
            
            # if it is ON THE LIST
            elif ch in char_list:
                
                # find its index
                index = char_list.index(ch)
                
                # increase its occurence by 1
                occurences[index]+=1
            
    # Now determine the winner.
    # step by step:
    # 1) find the maximum value of occurences
    # 2) get the index of it
    # 3) since the indexes are same, find corresponding character in char_list
    winner = char_list[occurences.index(max(occurences))]

    print("\nThe most frequently occuring letter is", winner, "with", max(occurences), "occurences.")
            
# call the main function
main()