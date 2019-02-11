# print the headings
print("Celsius\tFahrenheit")
print("------------------")

# calculate Fahrenheit using Celsius
for temp in range(21):
    fahren = 9/5 * temp + 32
    
    #display results on a table
    print(temp, "\t", format(fahren, ",.1f"))