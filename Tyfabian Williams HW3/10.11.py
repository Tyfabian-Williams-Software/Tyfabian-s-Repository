# Tyfabian Williams
# 2142655
class FoodItem:
    def __init__(self, food_name1='None', fat1=0.0, carbs1=0.0, protein1=0.0):
        self.name = food_name1
        self.fat = fat1
        self.carbs = carbs1
        self.protein = protein1

    def get_calories(self, num_servings1):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings1
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


if __name__ == '__main__':

    food1 = FoodItem()

    food_name = input()
    fat = float(input())
    carbs = float(input())
    protein = float(input())

    food2 = FoodItem(food_name, fat, carbs, protein)

    num_servings = float(input())
    food1.print_info()
    print(
        'Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings, food1.get_calories(num_servings)))
    print()
    food2.print_info()
    print(
        'Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings, food2.get_calories(num_servings)))
