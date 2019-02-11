# this program uses a loop to display a table of numbers and their squares

# get the ending limit
print("This program displays a list of numbers")
print("(starting at 1) and their squares.")
end = int(input("How high should I go? "))

# print the table headings
print("Number\tSquare")
print("---------------")

# print the numbers and their squares
for number in range(1, end+1):
    square = number**2
    print(number, "\t", square)