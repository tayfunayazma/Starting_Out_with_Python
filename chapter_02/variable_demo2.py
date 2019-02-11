# create two variables: top_speed and distance.
top_speed = 160
distance = 300

# display the values referenced by the variables.
print("The top speed is")
print(top_speed)
print("The distance traveled is")
print(distance) 

# exercise to add the value after print
print("The top speed is", top_speed)
print("The distance traveled is", distance)

print("The top speed is", top_speed, sep="\t")
print("The distance traveled is", distance, sep="  ")

print("The top speed is " + str(top_speed))
print("The distance traveled is\t" + str(distance))