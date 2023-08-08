from numbers import Real
from typing import Dict

from models.ingredient import Ingredient

Recipe = Dict[Ingredient, int]


class Dish:
    def __init__(self, name: str, price: float) -> None:
        self.name = name

        if not isinstance(price, Real):
            raise TypeError("Dish price must be float.")
        if price <= 0:
            raise ValueError("Dish price must be greater then zero.")

        self.price = price
        self.recipe: Recipe = {}

    def __repr__(self) -> str:
        return f"Dish('{self.name}', R${self.price:.2f})"

    def __eq__(self, other) -> bool:
        return self.__repr__() == other.__repr__()

    def __hash__(self) -> int:
        return hash(self.__repr__())

    def add_ingredient_dependency(self, ingredient: Ingredient, amount: int):
        self.recipe[ingredient] = amount

    def get_restrictions(self):
        return set(
            restriction
            for ingredient in self.recipe.keys()
            for restriction in ingredient.restrictions
        )

    def get_ingredients(self):
        return set(self.recipe.keys())


# Vamos criar alguns objetos Ingredient para usar nos pratos
# queijo = Ingredient("queijo")
# farinha = Ingredient("farinha")
# camarao = Ingredient("camarão")
# cebola = Ingredient("cebola")


# # Vamos criar os pratos
# prato1 = Dish("Pizza", 25.0)
# prato2 = Dish("Risoto", 30.0)

# Vamos adicionar ingredientes aos pratos usando o método add_ingre
# prato1.add_ingredient_dependency(queijo, 2)
# prato1.add_ingredient_dependency(farinha, 1)
# prato1.add_ingredient_dependency(cebola, 1)

# prato2.add_ingredient_dependency(farinha, 1)
# prato2.add_ingredient_dependency(camarao, 10)
# prato2.add_ingredient_dependency(cebola, 2)

# Vamos verificar as restrições dos pratos usando o método get_restrictions()
# print("Restrições do prato 1:", prato1.get_restrictions())
# print("Restrições do prato 2:", prato2.get_restrictions())

# Vamos verificar os ingredientes dos pratos usando o método get_ingredien
# print("Ingredientes do prato 1:", prato1.get_ingredients())
# print("Ingredientes do prato 2:", prato2.get_ingredients())

# print(prato1.recipe)
