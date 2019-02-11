# this program converts km to miles

def main():
    distance = float(input("Enter a distance in km: "))
    miles = convert_km_mile(distance)
    print("The distance", distance, "in km is", miles )
    
def convert_km_mile(distance):
    return distance * 0.6214
    
# call the main function
main()