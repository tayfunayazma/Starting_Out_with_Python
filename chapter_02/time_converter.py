# get a number of seconds from the user
total_seconds = float(input("Enter a number of seconds: "))

# get the number of hours
hours = total_seconds//3600

# get the number of remaining minutes
minutes = (total_seconds // 60) % 60

# get the number of remaining seconds
seconds = total_seconds % 60

# display the result
print("Here is the time in hours, minutes, and seconds: ")
print("Hours: ", hours)
print("Minutes: ", minutes)
print("Seconds: ", seconds)