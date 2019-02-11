# hot dog cook-out calculator

# ask the user the number of people attending the cook-out
people = int(input("How many people will be attending the cook-out?: "))
num_hotdogs = int(input("How many hot dogs will be given to each person?: "))
total = people * num_hotdogs

# decision structure
# no leftover
if total%10 == 0 and total%8 == 0:
    print("You will need", total//10, "packs of hot dogs and", \
          total//8, "packs of buns")
    print("There will be no leftovers")
# leftover for hot dogs but no buns
elif total%10 != 0 and total%8 == 0:
    print("You will need", (total//10)+1, "packs of hot dogs and", \
          total//8, "packs of buns")
    print("There will be", 10-(total%10), "hot dogs leftover")
# leftover for buns but no hot dogs
elif total%10 == 0 and total%8 != 0:
    print ("You will need", total//10, "packs of hot dogs and", \
         (total//8)+1, "packs of buns")
    print("There will be", 8-(total%8), "buns leftover")
# both leftover
else:
    print("You will need", (total/10)+1, "packs of hot dogs and", \
          (total//8)+1,"packs of buns")
    print("There will be", 10-(total//10), "hot dogs leftover and", 8-(total//8), "buns leftover")
