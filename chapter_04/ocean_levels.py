# ocean is rising at 1.6 millimeters
rise = 1.6

# set the ocean level 0
ocean_level = 0

# set the starting year and ending year
start_year = 2019
end_year = 2044

# print the headings
print("Years\tOceal Level")
print("-------------------")

# calculate the ocean's level for each year
for i in range(start_year, end_year+1):
    ocean_level = ocean_level + 1.6
    print(i, "\t", format(ocean_level, ",.1f"))