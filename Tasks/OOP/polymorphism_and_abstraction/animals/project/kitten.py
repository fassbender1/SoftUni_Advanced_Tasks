from abc import ABC

from project.cat import Cat


class Kitten(Cat, ABC):
    def __init__(self, name: str, age: int, gender: str = "Female"):
        super().__init__(name, age, gender)
        self.gender = gender

    @staticmethod
    def make_sound():
        return f"Meow"