import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        with open(source_path, "r") as file:
            reader = csv.DictReader(file)
            dish_dict = {}

            for row in reader:
                dish = Dish(row["dish"], float(row["price"]))

                if dish.name not in dish_dict:
                    dish.add_ingredient_dependency(
                        Ingredient(row["ingredient"]),
                        int(row["recipe_amount"]),
                    )
                    dish_dict[dish.name] = dish
                else:
                    dish_dict[dish.name].add_ingredient_dependency(
                        Ingredient(row["ingredient"]),
                        int(row["recipe_amount"]),
                    )

        self.dishes = set(dish_dict.values())
