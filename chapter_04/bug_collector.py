# set an accumulator for the number of bugs
total = 0.0

# set a loop and accumulate the numbers
for day in range(5):
    print("Number of bugs collected on day", day+1, end="")
    num_bugs = int(input(": "))
    total += num_bugs
print("The total number of bugs collected is:", format(total, ".0f"))