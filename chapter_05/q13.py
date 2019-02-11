# this program calculates an object falling distance using 
# the formula d = (1/2)*g*t**2

# gravity as a constant
GRAVITY = 9.8

def main():
    # the headers of the table
    print("Seconds\t\tDistance")
    print("------------------------")
    for time in range(1,11):
        distance = falling_distance(time)
        print(time, "\t\t", format(distance, ",.2f"))

# distance calculation    
def falling_distance(time):
    distance = 1/2*GRAVITY*time**2
    return distance

# call the main function
main()
    