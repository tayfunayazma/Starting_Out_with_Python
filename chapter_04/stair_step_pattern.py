# this program displays a stair_step pattern
num_steps = 6

for r in range(num_steps):
    for c in range(r):
        print(" ", end="")
    print("#")