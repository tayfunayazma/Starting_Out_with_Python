# this program displays prime numbers from 1 through 100

def main():
    is_prime()


def is_prime():
    for num in range(2,101):
        # prime set to be true until it can falsified
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False 
        if prime:
            print(num)               
       
# call the main function    
main()
        