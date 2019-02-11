# this program displays the tuition amount for a yearly increase of 3 percent

tuition = 8000
increase_rate = 0.03

#print the headings
print("Years\tProjected Tuition")
print("-------------------------")

# calculate the projected tuition for the next 5 years
for i in range(1, 6):
    tuition = tuition + tuition * 0.03
    print(i, "\t", "$", format(tuition, ",.2f"), sep="")