# average number of words

def main():
    # open the file
    infile = open("text.txt", "r")
    
    # read the contents of the file
    lines = infile.readlines()
    
    # close the file
    infile.close()
    print(lines)
    
    # set accumulators for word count and line count
    line_count = 0
    total_word_count = 0
    
    
    # read each elements in lines list
    for line in lines:
        line_count += 1
        word_count = line.split()
        total_word_count += len(word_count)
        
    # calculate the average
    average = total_word_count / line_count
    print("Total words:", total_word_count)
    print("Total lines:", line_count)
    print("The average number of words per sentence is", format(average, ",.2f"))
    
# call the main function
main()    
    