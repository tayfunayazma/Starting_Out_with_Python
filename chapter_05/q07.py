# this program calculates the amount of income generated 
# from ticket sales

def main():
    classA = class_A()
    classB = class_B()
    classC = class_C()
    total_income(classA, classB, classC)
    
def class_A():
    tickets = int(input("How many tickets from Class A is sold? "))
    income_class_A = tickets * 20
    return income_class_A
    
def class_B():
    tickets = int(input("How many tickets from Class B is sold? "))
    income_class_B = tickets * 15
    return income_class_B

def class_C():
    tickets = int(input("How many tickets from Class C is sold? "))
    income_class_C = tickets * 10
    return income_class_C
    
def total_income(a,b,c):
    income = a + b + c
    print("The amount of income generated from ticket sales is $", \
          format(income, ",.2f"), sep="")

# call the main function    
main()
    