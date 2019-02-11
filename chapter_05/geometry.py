# this program allows the user to choose various 
# geometry calculations from a menu. This program
# imports the circle and rectangle modules
import circle
import rectangle

# constants for the menu choices
AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5

# the main function
def main():
    # the choice variable controls the loop 
    # and holds the user's menu choice
    
    choice = 0
    
    while choice != QUIT_CHOICE:
        # display the menu
        display_menu()
        
        # get the user's choice
        choice = int(input("Enter your choice: "))
        
        # perform the selected action
        if choice == AREA_CIRCLE_CHOICE:
            radius = float(input("Enter the circle's radius: "))
            print("The area is", circle.area(radius))
            print()
        elif choice == CIRCUMFERENCE_CHOICE:
            radius = float(input("Enter the circle's radius:"))
            print("The circumference is", \
                  circle.circumference(radius))
            print()
        elif choice == AREA_RECTANGLE_CHOICE:
            width = float(input("Enter the rectangle's width: "))
            length = float(input("Enter the rectangle's length: "))
            print("The area is", rectangle.area(width, length))
            print()
        elif choice == PERIMETER_RECTANGLE_CHOICE:
            width = float(input("Enter the rectangle's width: "))
            length = float(input("enter the rectangle's length: "))
            print("The perimeter is", \
                  rectangle.perimeter(width, length))
            print()
        elif choice == QUIT_CHOICE:
            print("Exiting the program...")
            print()
        else:
            print("Error: Invalid selection!")
            
# the display_menu function displays a menu            
def display_menu():
    print(" MENU")
    print("1) Area of a circle")
    print("2) Circumference of a circle")
    print("3) Area of a rectangle")
    print("4) Perimeter of a rectangle")
    print("5) Quit")
    
# call the main function
main()
         