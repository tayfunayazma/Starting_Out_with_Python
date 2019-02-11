# shipping charges

# ask the user to enter the weight of a package
weight_pac = float(input("Enter the weight of the package you want to ship: "))

# display the shipping charges
if weight_pac > 0 and weight_pac <= 2:
    print("The shipping charge is $", weight_pac*1.5, sep="")
elif weight_pac > 2 and weight_pac <= 6:
    print("The shipping charge is $", weight_pac*3, sep="")
elif weight_pac > 6 and weight_pac <= 10:
    print("The shipping charge is $", weight_pac*4, sep="")
elif weight_pac > 10:
    print("The shipping charge is $", weight_pac*4.75, sep="")
else:
    print("Error: Your entry is not correct")