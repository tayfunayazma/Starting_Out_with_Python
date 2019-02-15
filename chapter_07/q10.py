# world series champions

def main():
    # open the file in reading mode
    infile = open("WorldSeriesWinners.txt", "r")
    
    # read the contents of the file
    winners = infile.readlines()
    
    # close the file
    infile.close()
    
    # strip the \n from the elements
    index = 0
    while index < len(winners):
        winners[index] = winners[index].rstrip("\n")
        index += 1
        
    #print(winners)
    num_wins(winners)
     
def num_wins(winners):
    # ask the user to an the name of a team to search for
    team_name = input("Enter the name of a team: ")
    
    # initialize an accumulator to hold the number of wins
    total_win = 0
    index = 0
    while index < len(winners):
        if team_name == winners[index]:
            total_win += 1
        index += 1
    
    print(team_name, "has won the World Series for", total_win, "times in the time period from 1903 through 2009") 
       
# call the main function
main()