# date printer

def main():
    # ask the user to enter a date
    date_string = input("Enter a date in the form of mm/dd/yyyy: ")
    
    # split the date
    date_list = date_string.split("/")
    
    # create a months list
    months = ["January", "February", "March", "April", "May",
              "June", "July", "August", "September", "October",
              "November", "December"]
    
    # month
    months = str(months[int(date_list[0]) - 1]) # since months list first index = 0, 
                                                # we need to write months[int(date_list[0]) - 1] 
    
    # day
    day = date_list[1]
    
    # year
    year = date_list[2]
    
    print(months + " " + day + ", " + year)
    
        
# call the main function
main()