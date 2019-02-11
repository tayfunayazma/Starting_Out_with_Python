def main():
    number = int(input("Enter a number: "))
    if is_prime(number):
        print(number, "is prime")
    else:
        print(number, "is not prime")
    
def is_prime(number):
    # numbers less than 2 is not prime
    if number < 2:
        return False
    
    # the for loop divides the user's number by every number less than the user"s number
    # if it is divisible, then it is not prime
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

# call the main function
main()


# alternative way
#import math
#def main():
    #number = int(input("Enter a number: "))
    #num = is_prime(number)
    #if num == False:
        #print(number, "is not prime")
    #else:
        #print(number, "is prime")
    
#def is_prime(number):
    #if number < 2:
        #return False
    
    #for i in range(2, int(math.sqrt(number))+1):
        #if number % i == 0: 
            #return False
    #return True
        
#main()