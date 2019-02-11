# this program display two random numbers and ask the user to 
# calculate the sum of these numbers and it checks if the user's
# answer is correct

import random

def main():
    number1 = random.randint(1,1000)
    number2 = random.randint(1,1000)
    print("Please calculate the sum of the following numbers:")
    print(number1)
    print(number2)
    user_answer = int(input("Enter your answer here: "))
    sum_answer = sum_numbers(number1, number2)
    check_answer(user_answer, sum_answer)
    
def sum_numbers(number1, number2): 
    return number1 + number2   

def check_answer(user_answer, sum_answer): 
    if user_answer  == sum_answer:
        print("Congratulations. Your answer is correct")
    else:
        print("Wrong. The correct answer is", sum_answer)

# call the main function
main()