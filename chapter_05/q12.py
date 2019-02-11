# this program display the maximum of two values

def main():
    number1 = int(input("Enter an integer: "))
    number2 = int(input("Enter another integer: "))
    max_number = maximum_of_values(number1, number2)
    print(max_number)
    
def maximum_of_values(number1, number2):
    return max(number1, number2)

# call the main function    
main()