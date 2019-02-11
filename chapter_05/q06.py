# this program calculates calories from fat and carbohydrates

def main():
    fat_grams = float(input("Enter the fat grams: "))
    carbo_grams = float(input("Enter the carbohydrate grams: "))
    get_fat_calories(fat_grams)
    get_carbo_calories(carbo_grams)

# calculations to convert fat grams and carb grams to calories    
def get_fat_calories(fat_grams):
    fat_calories = fat_grams * 9
    print("The calories from fat is", fat_calories, "calories")
    
def get_carbo_calories(carb_grams):
    carbo_calories = carb_grams * 4
    print("The calories from carbs is", carbo_calories, "calories")

# call the main function    
main()