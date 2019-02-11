# this program display the number of calories burned
# after 10, 15, 20, 25, 30 minutes

cal_per_min = 4.2

# print the header
print("Minutes\t\tCalories")
print("------------------------")

for minutes in range(10,31,5):
    total = minutes * cal_per_min
    print(minutes, "minutes" "\t", total)