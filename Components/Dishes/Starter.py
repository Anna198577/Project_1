from .Dish import Dish

class Starter(Dish): 
    def __init__(self, name, price, description, ingredients, diet_type, cuisine):
        super().__init__(name, price, description, ingredients, diet_type, cuisine)