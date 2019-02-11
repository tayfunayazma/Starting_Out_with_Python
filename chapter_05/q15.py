# this program calculates student's test average and grade 
# display in a table

# itertools library imported to iterate two variables in for loop simultaneously 
#import itertools

def main():
    test1 = int(input("Enter the score for test 1: "))
    test2 = int(input("Enter the score for test 2: "))
    test3 = int(input("Enter the score for test 3: "))
    test4 = int(input("Enter the score for test 4: "))
    test5 = int(input("Enter the score for test 5: "))
    print()
    print("Test No\t\tScore\t\tGrade")
    print("-------------------------------------")
    determine_grade(test1, test2, test3, test4, test5)
    print()
    average = calc_average(test1, test2, test3, test4, test5)
    print("The average is", format(average, ",.2f"))
    
def calc_average(test1, test2, test3, test4, test5):
    return (test1 +test2 + test3 + test4 + test5)/5

# i and grade variables iterate simultaneously in for loop    
def determine_grade(test1, test2, test3, test4, test5):
    for i, grade in zip(range(1,6), (test1, test2, test3, test4, test5)):
            if grade >= 90 and grade <= 100:
                print(i, "\t\t", grade, "\t\t A")
            elif grade >= 80 and grade <= 89:
                print(i, "\t\t", grade, "\t\t B")
            elif grade >= 70 and grade <= 79:
                print(i, "\t\t", grade, "\t\t C")
            elif grade >= 60 and grade <= 69:
                print(i, "\t\t", grade, "\t\t D")
            elif grade >= 0 and grade < 60:
                print(i, "\t\t", grade, "\t\t F")
            else:
                print("Error: Invalid entry")

# call the main function    
main()