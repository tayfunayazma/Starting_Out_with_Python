# software sales

# ask the user to enter the number of packages purchased
num_packs = int(input("Enter the number of packages purchased: "))

# display the amount of discount and total amount of purchase after the discount
if num_packs > 0 and num_packs <= 10:
    print("The amount of discount is $", format(num_packs*99*0, ",.2f"), sep="")
    print("The total amount of purchase is $", format(num_packs*99, ",.2f"), sep="")
elif num_packs >= 10 and num_packs <= 19:
    print("The amount of discount is $", format(num_packs*99*0.1, ",.2f"), sep="")
    print("The total amount of purchase is $", format(num_packs*99-(num_packs*99*0.1), ",.2f"), sep="")
elif num_packs >= 20 and num_packs <= 49:
    print("The amount of discount is $", format(num_packs*99*0.2, ",.2f"), sep="")
    print("The total amount of purchase is $", format(num_packs*99-(num_packs*99*0.2), ",.2f"), sep="")
elif num_packs >= 50 and num_packs <= 99:
    print("The amount of discount is $", format(num_packs*99*0.3, ",.2f"), sep="")
    print("The total amount of purchase is $", format(num_packs*99-(num_packs*99*0.3), ",.2f"), sep="")
elif num_packs >= 100:
    print("The amount of discount is $", format(num_packs*99*0.4, ",.2f"), sep="")
    print("The total amount of purchase is $", format(num_packs*99-(num_packs*99*0.4), ",.2f"), sep="")
else:
    print("Error:You entry is not correct")