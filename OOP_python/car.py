
class Engine:
    def __init__(self, horsepower, fuel_type):
        self.horsepower = horsepower
        self.fuel_type = fuel_type

    def start(self):
        print("Engine started")

    def stop(self):
        print("Engine stopped")


class Car(Engine):
    def __init__(self, make, model, year, horsepower, fuel_type):
        self.make = make
        self.model = model
        self.year = year
        super().__init__(horsepower, fuel_type)

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

# Create an object of the Car class
my_car = Car("Toyota", "Camry", 2022)

# Call the method
my_car.display_info()