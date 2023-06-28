import json

class Dish: 
    def __init__(self, name, price, description, ingredients, diet_type, cuisine):
        self.name = name
        self.price = self.serialize_price(price) if type(price) != dict else price
        self.description = description
        self.ingredients = [ingredient.strip() for ingredient in ingredients.split(",")] if type(ingredients) != list else ingredients
        self.diet_type = diet_type
        self.cuisine = cuisine

    def serialize_price(self, price: list[str] | str) -> dict:
        prices = {
            "price_usd" : None,
            "price_pln" : None,
            "price_eur" : None
        }

        if type(price) == list:
            for p in price:
                p = p.split()[0]
                if "USD" in p:
                    prices["price_usd"] = float(p)
                elif "PLN" in p:
                    prices["price_pln"] = float(p)
                elif "EUR" in p:
                    prices["price_eur"] = float(p)
        elif type(price) == str:
            if "USD" in price:
                prices["price_usd"] = float(price.split()[0])
                prices["price_pln"] = self.to_pln(price)
                prices["price_eur"] = self.to_eur(price)
            elif "PLN" in price:
                prices["price_pln"] = float(price.split()[0])
                prices["price_usd"] = self.to_usd(price)
                prices["price_eur"] = self.to_eur(price)
            elif "EUR" in price:
                prices["price_eur"] = float(price.split()[0])
                prices["price_usd"] = self.to_usd(price)
                prices["price_pln"] = self.to_pln(price)


        # Zaokrąglanie do dwóch miejsc po przecinku
        for k,v in prices.items():
            prices[k] = round(v, 2)

        return prices

    def to_usd(self, price: str) -> float:
        # Jeśli podana wartość jest w zł, to zamieniamy na usd ze zł
        # Zmienia zł na usd, eur na usd
        if "PLN" in price:
        # przeliczamy ceny w złotówkach na dolary amerykańskie
            price = float(price.split()[0]) / 3.8  # przyjmujemy kurs 1 USD = 3.8 PLN
        elif "EUR" in price:
            # przeliczamy ceny w euro na dolary amerykańskie
            price = float(price.split()[0]) * 1.18  # przyjmujemy kurs 1 USD = 1.18 EUR
        return price

    def to_pln(self, price: str) -> float:
        # Jeśli podana wartość jest w $, to zamieniamy z usd na zł
        # Zmienia usd na zł, eur na zł
        if "USD" in price:
            price = float(price.split()[0]) * 3.8
        elif "EUR" in price:
            price = float(price.split()[0]) * 4.5
        return price

    def to_eur(self, price: str) -> float:
        if "USD" in price:
            price = float(price.split()[0]) * 1.18
        elif "PLN" in price:
            price = float(price.split()[0]) / 4.5
        return price

    def get_dictionary_data(self):
        dish_dictionary = {
            "name" : self.name,
            "price" : self.price,
            "description" : self.description,
            "ingredients" : self.ingredients,
            "diet_type" : self.diet_type,
            "cuisine" : self.cuisine
        }
        return dish_dictionary

    def get_tuple_data(self):
        dish_tuple = (
            self.name,
            self.price["price_usd"],
            self.price["price_pln"],
            self.price["price_eur"],
            self.description,
            json.dumps(self.ingredients),
            self.diet_type,
            self.cuisine
        )
        return dish_tuple