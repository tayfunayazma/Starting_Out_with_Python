# this program converts speed in kph to mph using a for loop

# print the table headings
print("KPH\tMPH")
print("---------")

# print the kph and it's equal in mph
for kph in range(60, 131, 10):
    mph = kph*0.6212
    print(kph, "\t", format(mph, ".1f"))