# this program simulates rock, paper, scissors game

import random

def main():
    print("Possible options are:")
    print("1) Rock")
    print("2) Paper")
    print("3) Scissors")
    print()
    
    # if it is a draw, the computer prompts the user to enter a new choice
    status = True
    while status == True:
        number = get_random_number()
        user_choice = int(input("Enter your choice of 'rock', 'paper' or 'scissors' as a number: "))
        print()
        computer_choice(number)
        show_user_choice(user_choice)
        status = compare_choices(number, user_choice)
    

def get_random_number():
    number = random.randint(1,3)
    return number
    
def computer_choice(number):
    if number == 1:
        print("Computer chooses rock.")
    elif number == 2:
        print("Computer chooses paper.")
    else:
        print("Computer chooses scissors.")
        
def show_user_choice(user_choice):
    if user_choice == 1:
        print("You choose rock.")
    elif user_choice == 2:
        print("You choose paper.")
    else:
        print("You choose scissors.")

    
def compare_choices(number, user_choice):
    print()
    # status set to be false to repeat the process if it is not false
    status = False
    
    if number==1 and user_choice==3:
        print("You lost. Rock smashes scissors.")
    elif number==3 and user_choice==1:
        print("You won. Rock smashes scissors.")
    elif number==1 and user_choice==2:
        print("You won. Paper wraps rock.")
    elif number==2 and user_choice==1:
        print("You lost. Paper wraps rock")
    elif number==2 and user_choice==3:
        print("You won. Scissors cuts paper.")
    elif number==3 and user_choice==2:
        print("You lost. Scissors cuts paper.")
    elif number==user_choice:
        print("*****It is a draw try again*****")
        status = True     
    return status           
        
main()