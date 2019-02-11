# book club points example

# ask the user to enter the number of books purchased this month
num_books = int(input("Enter the number of books purchased this month: "))

# display the number of points
if num_books == 0:
    print("You earn 0 points")
elif num_books >= 2 and num_books < 4:
    print("You earn 2 points")
elif num_books >= 4 and num_books < 6:
    print("You earn 15 points")
elif num_books >= 6 and num_books < 8:
    print("You earn 30 points")
elif num_books > 8:
    print("You earn 60 points")
else:
    print("Error: You entered an invalid number")
    