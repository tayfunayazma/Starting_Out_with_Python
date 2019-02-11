# this program calculates the average of numbers
# stored in names.txt file
def main():
    try:
        # open the file
        infile = open("numbers.txt", "r")
        
        # initialize an accumulator
        total = 0.0
        
        # initialize a variable to keep the count of the lines
        count = 0
        
        for line in infile:
            line = float(line)
            print(line)
            
            # add 1 to the count variable
            count += 1
            
            # calculate the sum of the numbers
            total += line
        
        # close the file
        infile.close()
        
        # calculate the average and display
        average_num = total / count
        print("The average of the numbers stored in the file is", average_num)
    
    # this is exception in case there is 0 number in the file    
    except ZeroDivisionError:
        print("ERROR: There is no number in the file")
    
    except ValueError:
        print("ERROR: The file has non-numeric content")
        
    except IOError:
        print("No such file or directory")
        
# call the main function
main()
        