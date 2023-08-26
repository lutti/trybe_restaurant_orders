from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1 - Lutti
def test_ingredient():
    ing_1 = Ingredient("picanha")
    ing_2 = Ingredient("setinho")
    ing_3 = Ingredient("picanha")

    assert ing_1.name == "picanha"
    assert ing_1.restrictions == set()

    assert hash(ing_1) != hash(ing_2)
    assert hash(ing_1) == hash(ing_3)

    assert ing_1 == ing_3
    assert ing_1 != ing_2

    assert repr(ing_1) == "Ingredient('picanha')"
