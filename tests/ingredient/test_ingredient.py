from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


def test_ingredient():

    ingrediente = Ingredient("mandioca")
    assert isinstance(ingrediente, Ingredient)
    assert ingrediente.name == "mandioca"

    ingredient1 = Ingredient('mandioca')
    ingredient2 = Ingredient('frango')
    ingredient3 = Ingredient('ovo')

    assert ingredient1.restrictions == set()
    assert ingredient2.restrictions == {
        Restriction.ANIMAL_MEAT, Restriction.ANIMAL_DERIVED}
    assert ingredient3.restrictions == {Restriction.ANIMAL_DERIVED}

    ingrediente = Ingredient("alho")
    assert repr(ingrediente) == "Ingredient('alho')"

    ingrediente1 = Ingredient("couve")
    ingrediente2 = Ingredient("couve")
    ingrediente3 = Ingredient("frango")

    assert ingrediente1 == ingrediente2
    assert ingrediente1 != ingrediente3

    ingrediente1 = Ingredient("frango")
    ingrediente2 = Ingredient("frango")
    ingrediente3 = Ingredient("camarao")

    assert hash(ingrediente1) == hash(ingrediente2)
    assert hash(ingrediente1) != hash(ingrediente3)
        

    