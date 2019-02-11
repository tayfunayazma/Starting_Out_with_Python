# this program determines whether a bank customer
# qualifies for a loan

min_salary = 30000.0    # the minimum annual salary
min_years = 2           # the minimum years on the job

# get the customer's annual salary
salary = float(input("Enter your annual salary: "))

# get the number of years on the current job
years_on_job = int(input("Enter the number of" +
                         "years employed: "))

# determine whether the customer qualifies
if salary >= min_salary:
    if years_on_job >= min_years:
        print("You qualify the for the loan")
    else:
        print("You must have been employed", \
              "for at least", min_years, \
              "years to qualify.")
else:
    print("You must earn at least $", \
          format(min_salary, ",.2f"), \
          " per year to qualify.", sep="")
        