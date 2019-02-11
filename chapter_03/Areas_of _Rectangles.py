# areas of rectangles example

# ask the length and width of the rectangles
length1 = float(input("Enter the length of the first rectangle: "))
width1 = float(input("Enter the width the first rectangle: "))
length2 = float(input("Enter the length of the second rectangle: "))
width2 = float(input("Enter the width of the second rectangle: "))

# calculate the area of the rectangles
area1 = length1 * width1
area2 = length2 * width2

# determine which rectangle is bigger
if area1 > area2:
    print("Rectangle 1 is bigger than rectangle 2")
elif area1 == area2:
    print("Rectangles are the same size")
else:
    print("Rectangle 2 is bigger than rectangle 1")