# feet to inches

def main():
    number_feet = float(input("Enter a number of feet: "))
    feet_to_inches(number_feet)


def feet_to_inches(feet):
    inches = feet * 12
    print(feet, "feet equals to", inches, "inches")
    return inches

# call the main function
main()