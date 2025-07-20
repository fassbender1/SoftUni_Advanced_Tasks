from abc import ABC
from project.cat import Cat


class Tomcat(Cat, ABC):
    def __init__(self, name: str, age: int, gender: str = "Male"):
        super().__init__(name, age, gender)
        self.gender = gender

    @staticmethod
    def make_sound():
        return f"Hiss"