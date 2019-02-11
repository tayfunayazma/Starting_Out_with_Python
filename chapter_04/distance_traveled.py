# ask the user to enter the speed and the number of hours traveled
speed = int(input("What is the speed of the vehicle in mph? "))
hours = int(input("How many hours has it traveled? "))

# print the headings
print("Hours\tDistance traveled")
print("-------------------------")

# set a loop to display speed with hours
for hours in range(1, hours+1):
    distance = speed * hours
    print(hours, "\t", distance)