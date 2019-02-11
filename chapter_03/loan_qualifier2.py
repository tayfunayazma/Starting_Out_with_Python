# this program determines whether a bank customer 
# qualifies for a loan

min_salary = 30000.0    # the minimum annual salary
min_years = 2           # the minimum years on the job

# get the customer's annual salary
salary = float(input("Enter your annual salary: "))

# get the number of years on the current job
years_on_job = int(input("Enter the number of years" +
                         " employed: "))

# determine whether the customer qualifies
if salary >= min_salary and years_on_job >= 2:
    print("You qualify for the loan")
else:
    print("You do not qualify", \
           "for this loan")