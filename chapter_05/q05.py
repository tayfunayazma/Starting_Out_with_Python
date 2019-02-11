# this program calculates property tax 

def main():
    property_value = float(input("Enter the value of your property: "))
    assessment = property_assessment(property_value)
    property_tax(assessment)
       
def property_assessment(value):
    assessment = value * 0.60
    print("The property assessment is $", format(assessment, ",.2f"), sep="")
    return assessment
    
def property_tax(assessment):
    tax = (assessment * 0.72)/100
    print("The property tax is $", format(tax, ",.2f"), sep="")

# call the main function
main()