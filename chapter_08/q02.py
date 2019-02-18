# sum of digits in a string
def main():
    number = input("Enter a series of single-digit numbers: ")
    sum = 0
    for ch in number:
        sum += int(ch)
        
    print("The sum of the digits in the number is:", sum)
# call the main function
main()