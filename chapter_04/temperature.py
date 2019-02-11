# this program guides the technician in process of checking a substance's temperature

# create a variable to represent the maximum temperature
max_temp = 102.5

# get the substance's temperature
sub_temp = float(input("Enter the substance's temperature: "))

# as long as necessary instruct the user to adjust the thermostat
while sub_temp > max_temp:
    print("Turn down the thermostat, wait 5 minutes, and check the temperature again")
    sub_temp = float(input("Enter the new substance's temperature: "))
    
print("Temperature is acceptable. Check it again in 15 minutes")