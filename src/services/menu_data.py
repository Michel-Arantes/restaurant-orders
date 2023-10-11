import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        pass
        dishes = dict()
        with open(source_path) as csvfile:
            rows = csv.reader(csvfile)
            next(rows)
            for dish, price, ingredient, recipe_amount in rows:
                if dish not in dishes:
                    dishes[dish] = Dish(dish, float(price))
                dishes[dish].add_ingredient_dependency(
                    Ingredient(ingredient), int(recipe_amount)
                )
        self.dishes = set(dishes.values())

    def __iter__(self):
        return iter(self.dishes)

    def __next__(self):
        for dish in self:
            yield dish
        raise StopIteration