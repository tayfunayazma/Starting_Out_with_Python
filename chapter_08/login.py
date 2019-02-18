# the get_login function accepts a first name,
# last name and ID number as arguments. It returns
# a system login name

def get_login_name(first, last, idnumber):
    # get the first three letters of the first name
    # if name is less than 3 characters, the
    # slice will return the entire first name
    set1 = first[0 : 3]
    
    # get the first three letters of the last name
    # if the name is less than 3 characters, the
    # slice will return the entire last name
    set2 = last[0 : 3]
    
    # get the last three characters of the student ID
    # if the ID number is less than 3 characters, the
    # slice will return the entire ID number
    set3 = idnumber[-3 :]
    
    # put the sets of characters together
    login_name = set1 + set2 + set3
    
    # return the login name
    return login_name