class Flower:
    def __init__(self, name: str, water_requirements: float):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = False

    def water(self, quantity: float) -> None:
        if quantity >= self.water_requirements:
            self.is_happy = True

    def status(self) -> str:
        return f"{self.name} is {'' if self.is_happy else 'not '}happy"

flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
flower.water(100)
print(flower.status())

