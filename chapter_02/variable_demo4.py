# this program demonstrates variable reassignment.
# assign a value to the dollars variable.
dollars = 2.75
print("I have", dollars, "in my account")

# adding $ sign before the variable and sep and end functions
print("I have $", dollars, sep="",end="")
print(" in my account") 

# f literal
print(f"I have ${dollars} in my account")

# reassign dollars so it references a different value
dollars = 99.5
print("But now I have", dollars, "in my account")

# the same exercise above
print("But now I have $", dollars, sep="", end="")
print(" in my account")
print(f"But now I have ${dollars} in my account")