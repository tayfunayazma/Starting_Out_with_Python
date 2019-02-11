# this program displays the following patter

# ********
# *******
# ******
# *****
# ****
# ***
# **
# *

base_size = 8

for r in range(base_size+1, 0, -1):
    for c in range(r, 1, -1):
        print("*", end="")
    print()