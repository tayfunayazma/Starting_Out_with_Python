# time calculator example

# ask the user to enter a number of seconds
user_seconds = int(input("Enter a number of seconds: "))

# display the minutes, hours, and days in a given number of seconds
if user_seconds >= 60 and user_seconds < 3600:
    mins = user_seconds//60
    print("There is", mins, "minutes in", user_seconds, "seconds")
elif user_seconds >= 3600 and user_seconds < 86400:
    hours = user_seconds//3600
    print("There is", hours, "hours in", user_seconds, "seconds")
elif user_seconds >= 86400:
    days = user_seconds//86400
    print("There is", days, "days in", user_seconds, "seconds")
    
else:
    print("Error")