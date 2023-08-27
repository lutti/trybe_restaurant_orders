import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction


# Req 2
def test_dish():
    dish1 = Dish("Arroz Carreteiro", 25.50)
    dish2 = Dish("Arroz Carreteiro", 25.50)
    dish3 = Dish("Prato executivo", 35.90)

    assert dish1.name == "Arroz Carreteiro"
    assert dish1.price == 25.50
    assert dish1.recipe == {}

    assert hash(dish1) != hash(dish3)
    assert hash(dish1) == hash(dish2)

    assert dish1 == dish2
    assert dish1 != dish3

    assert repr(dish1) == "Dish('Arroz Carreteiro', R$25.50)"

    with pytest.raises(TypeError):
        Dish("Prato inválido", "string")

    with pytest.raises(ValueError):
        Dish("Prato inválido 2", -1)

    ing1 = Ingredient("picanha")
    ing2 = Ingredient("feijao")
    dish1.add_ingredient_dependency(ing1, 3)

    assert ing1 in dish1.recipe
    assert ing2 not in dish1.recipe
    assert dish1.recipe[ing1] == 3

    ing3 = Ingredient("farinha")
    dish1.add_ingredient_dependency(ing3, 1)

    assert dish1.get_restrictions() == {Restriction.GLUTEN}
    assert dish1.get_ingredients() == {ing1, ing3}
