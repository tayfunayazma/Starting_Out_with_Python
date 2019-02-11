num_males = int(input("Enter the number of males registered: "))
num_females = int(input("Enter the number of females registered: "))
total_student = num_males + num_females
per_males = num_males / total_student
per_females = num_females / total_student
print("The percentage of males is", format(per_males, ".0%"))
print("The percentage of females is", format(per_females, ".0%"))