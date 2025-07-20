from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return f"woof woof"

class Cat(Animal):
    def make_sound(self):
        return f"meow, meow"

class Frog(Animal):
    def make_sound(self):
        return f"frog sounds"

def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
