from project.food import Food

class Fruit(Food):
    def __init__(self, name: str, expiration_date: str):
        super().__init__(expiration_date)
        self.name = name
        self.expiration_date = expiration_date