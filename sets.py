from sets_categories_data import ALCOHOLS


def clean_ingredients(dish_name, dish_ingredients):

    ingredients = set(dish_ingredients)

        return (dish_name, dish_ingredients)


def check_drinks(drink_name, drink_ingredients):

    alcohols = ALCOHOLS 

    ingredients = set(drink_ingredientes)

    interseccion = ingredients.intersection(alcohols)

    if len(interseccion) == 0:

        return f"{drink_name} Mocktail"

    else:

        return f"{drink_name} Cocktail"
