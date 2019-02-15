# population data
START_YEAR = 1951

def main():
    # open the USPopulation.txt file
    infile = open("USPopulation.txt", "r")
    
    # read the contents of the file
    pop_list = infile.readlines()
    
    # close the file
    infile.close()
    
    # convert the contents to integer and strip \n
    index = 0
    while index < len(pop_list):
        pop_list[index] = int(pop_list[index].rstrip("\n"))
        index += 1
    
    annual_change(pop_list)
    
def annual_change(pop_list):
    # create an empty list
    ann_change = [0] * (len(pop_list)-1)
    
    index = 0
    
    # calculate the total yearly change
    while index < (len(pop_list)-1):
        ann_change[index] = pop_list[index+1] - pop_list[index]
        index += 1
    
    # calculate the average annual change in population
    total = 0
    for num in ann_change:
        total += num
    average = total / len(ann_change)
    print("The average annual change in population during the time period is", \
          format(average, ",.2f"))
    
    # display the year with the greatest increase
    print("The year with the greatest increase is", ann_change.index(max(ann_change)) +
           START_YEAR, "with an increase of", max(ann_change))
    print("The year with the smallest increase is", ann_change.index(min(ann_change)) +
           START_YEAR, "with an increase of", min(ann_change))
    

# call the main function
main()        