# this program display the following pattern

# ##
# # #
# #  #
# #   #
# #    #
# #     #
# #      #

num_steps = 6

for r in range(num_steps):
    print("#", end="")
    for c in range(r):
        print(" ", end="")
    print("#")