import csv
from models.dish import Dish
from models.ingredient import Ingredient
csv_file_path = 'data/menu_base_data.csv'


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = self.get_dishes(source_path)

    def get_dishes(self, path):
        dishes = {}
        with open(path, "r") as file:
            reader = csv.reader(file)
            next(reader)

            for line in reader:
                dish_name, price, ingredient_name, recipe_amount = line

                if dish_name not in dishes:
                    dishes[dish_name] = Dish(dish_name, float(price))

                ingredient = Ingredient(ingredient_name)
                dishes[dish_name].add_ingredient_dependency(
                    ingredient, int(recipe_amount)
                )

        return set(dishes.values())


menu = MenuData(csv_file_path)

for dish in menu.dishes:
    print(dish)
