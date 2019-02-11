# this program uses a loop to display a table of number and their squares

# get the starting value
print("This program displays a list of numbers")
print("and their squares.")
start = int(input("Enter the starting number: "))

# get the ending limit
end = int(input("How high should I go? "))

# print the table headings
print()
print("Number\tSquare")
print("--------------")

# print the numbers and their squares
for number in range(start, end+1):
    square = number**2
    print(number, "\t", square)
    
# example to generate a sequence goes from highest to lowest and "end" function
print()
for num in range(5,0,-1):
    print(num, end=" ")