# magic dates example

# ask user to enter a month/day/year in numeric form
month = int(input("Enter a month in a numeric form: "))
day = int(input("Enter a day in numeric form: "))
year = int(input("Enter a two-digit year: "))

# determine if the date is magic
if month * day == year:
    print ("The date is magic")
else:
    print("The date is not magic")