# this program gets three test scores and displays
# their average. It congratulates the user if the
# average is a high score

# the high score variable holds the value that is 
# considered a high score
high_score = 95

# get the three test scores
test1 = int(input("Enter the score for the test 1: "))
test2 = int(input("Enter the score for the test 2: "))
test3 = int(input("Enter the score for the test 3: "))

# calculate the average test score
average = (test1 + test2 + test3)/3

#print the average
print("The average score is ", average)

# if the average is a high score,
# congratulate the user
if average >= high_score:
    print("Congratulations")
    print("That is a great job")