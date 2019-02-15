# larger than n

def main():
    # create a list with some number in it
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # determine the number
    number = 3
    determine_greater(num_list, number)
        
def determine_greater(num_list, number):
    
    # create a second list
    list2 = []
    
    # append the numbers that are greater than the number=5 into 
    # the list two
    for num in num_list:
        if num > number:
            list2.append(num)
    print(list2)
    
# call the main function
main()