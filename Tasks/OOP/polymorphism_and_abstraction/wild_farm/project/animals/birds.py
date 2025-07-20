from project.animal.animal import Bird
from project.food import Food, Meat, Fruit, Vegetable, Seed


class Owl(Bird):
    @property
    def can_eat_food(self):
        return [Meat]

    @property
    def weight_increase(self):
        return 0.25

    @staticmethod
    def make_sound():
        return f"Hoot Hoot"

class Hen(Bird):
    @property
    def can_eat_food(self):
        return [Vegetable, Meat, Fruit, Seed]

    @property
    def weight_increase(self):
        return 0.35

    @staticmethod
    def make_sound():
        return f"Cluck"
