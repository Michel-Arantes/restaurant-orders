from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():    

    pizza = Dish('pizza', 45.00)
    risoto = Dish('risoto', 48.50)

    queijo = Ingredient("queijo")
    farinha = Ingredient("farinha")
    
    pizza.add_ingredient_dependency(queijo, 4)
    pizza.add_ingredient_dependency(farinha, 2)

    assert pizza == pizza
    assert pizza != risoto

    assert hash(pizza) == hash(pizza)
    assert hash(pizza) != hash(risoto)

    assert repr(pizza) == "Dish('pizza', R$45.00)"

    assert pizza.name == "pizza"

    assert pizza.price == 45.00

    assert pizza.recipe.get(queijo) == 4

    with pytest.raises(TypeError, match=r"Dish price must be float."):
        Dish("pizza", '45')

    with pytest.raises(
        ValueError,
        match=r"Dish price must be greater then zero."
    ):
        Dish("pizza", -45.00)

    assert pizza.get_restrictions() == {
        Restriction.GLUTEN
    }

    assert pizza.get_ingredients() == {queijo, farinha}
