from project.vehicle import Vehicle


class Car(Vehicle):
    DEFAULT_FUEL_CONSUMPTION: float = 3

    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)