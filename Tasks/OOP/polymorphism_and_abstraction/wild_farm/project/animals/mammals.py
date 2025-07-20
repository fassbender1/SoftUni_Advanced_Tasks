from project.animal.animal import Mammal
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    @property
    def can_eat_food(self):
        return [Vegetable, Fruit]

    @property
    def weight_increase(self):
        return 0.10

    @staticmethod
    def make_sound():
        return f"Squeak"

class Dog(Mammal):
    @property
    def can_eat_food(self):
        return [Meat]

    @property
    def weight_increase(self):
        return 0.40

    @staticmethod
    def make_sound():
        return f"Woof!"

class Cat(Mammal):
    @property
    def can_eat_food(self):
        return [Vegetable, Meat]

    @property
    def weight_increase(self):
        return 0.30

    @staticmethod
    def make_sound():
        return f"Meow"

class Tiger(Mammal):
    @property
    def can_eat_food(self):
        return [Meat]

    @property
    def weight_increase(self):
        return 1.00

    @staticmethod
    def make_sound():
        return f"ROAR!!!"