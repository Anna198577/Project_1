import json, os, datetime
from .Dishes.Dish import Dish

def validate_dish_input(dish: dict) -> bool:
    warunek_1 = dish["name"].replace(' ', '').isalpha()
    warunek_2 = isinstance(dish["name"], str)
    warunek_3 = len(dish["name"]) > 0 and len(dish["name"]) <= 32
    if not (warunek_1 and warunek_2 and warunek_3):
        return False

    for price in dish["price"]:
        warunek_1 = isinstance(dish["price"][price],float)
        warunek_2 = dish["price"][price] > 0 and dish["price"][price] <= 250
        if not (warunek_1 and warunek_2):
            return False

    warunek_1 = len(dish["description"]) > 0 and len(dish["description"]) <= 300
    warunek_2 =  len({'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}.intersection(set(dish["description"]))) == 0
    warunek_3 = isinstance(dish["description"], str)
    if not (warunek_1 and warunek_2 and warunek_3):
        return False

    if len(dish["ingredients"]) > 0:
        for ingredient in dish["ingredients"]:
            warunek_1 = len(ingredient) > 0
            warunek_2 = isinstance(ingredient, str)
            warunek_3 = len({'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}.intersection(set(ingredient))) == 0
            if not (warunek_1 and warunek_2 and warunek_3):
                return False

    if not dish["diet_type"] in ["Vegan", "Vegetarian", "Meat"]:
        return False 
    if not dish["cuisine"] in ["Bulgarian", "Italian", "Polish", "Spain", "Ukrainian"]:
        return False

    return True

def login_user(username: str, password: str, connector) -> bool:
    # Nie ma takiego loginu ktory ma mniej niz 6 znakow w username i mniej niz 4 znaki w password
    if len(username) < 6 or len(password) < 4:
        return False
    if connector.validate_user(username, password):
        connector.update_user_login_time(username)
        return True
    return False


def validate_registration_input(username, password, confirm_password):
    if len(password) < 4 or len(confirm_password) < 4:
        return "Hasło jest zbyt krótkie. Minimum to 4 znaki."
    if password != confirm_password:
        return "Hasła nie są identyczne."
    if len(username) < 6:
        return "Nazwa użytkownika jest zbyt krótka. Minimum to 6 znaków."
    if username[0].isdigit():
        return "Nazwa użytkownika nie może zaczynać się cyfrą."
    if not all(c.isalnum() or c in "-_." for c in username):
        return "Nazwa użytkownika zawiera niedozwolone znaki."
    return None

def logout_user(username: str, connector):
    connector.update_user_logout_time(username)