# color mixer example

# ask user to enter the names of two primary colors to mix (red, blue, yellow)
color1 = input("Enter a primary color among red, blue, and yellow to mix: ")
color2 = input("Enter another primary color among red, blue, and yellow to mix: ")

# determine which secondary color the user will get
# purple
if color1 == "red" and color2 == "blue":
    print("You get purple")
elif color1 == "blue" and color2 == "red":
    print ("You get purple")
# orange    
elif color1 == "red" and color2 =="yellow":
    print("You get orange")
elif color1 == "yellow" and color2 == "red":
    print("You get orange")
# green    
elif color1 == "blue" and color2 == "yellow":
    print("You get green")
elif color1 == "yellow" and color2 == "blue":
    print("You get green")
else:
    print("Error: Choose the colors given above")