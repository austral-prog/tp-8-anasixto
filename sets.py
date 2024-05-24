from sets_categories_data import (ALCOHOLS)


def clean_ingredients(dish_name, dish_ingredients):

    ingredients = set(dish_ingredients)

        return (dish_name, dish_ingredients)


def check_drinks(drink_name, drink_ingredients):

    alcohols = {}

    ingredients = set(drink_ingredientes)

    if ingredientes in alcohols:

        return drink_name + "Cocktail"

    else:

        return drink_name + "Mocktail"
