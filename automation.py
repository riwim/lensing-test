class Boat:

    def __init__(self, fuel):
        self.fuel = fuel

    def add_fuel(self, amount):
        self.fuel += amount

    def get_fuel(self):
        return self.fuel

my_boat = Boat(12)
my_boat.add_fuel(2)
my_boat.add_fuel(3)
print(my_boat.get_fuel())

