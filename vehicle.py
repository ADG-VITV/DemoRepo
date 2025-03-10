class Vehicle:
    def _init_(self, brand, model):
        self.brand = brand
        self.model = model
    
    def start_engine(self):
        print(f"{self.brand} {self.model} engine started.")
    
    def stop_engine(self):
        print(f"{self.brand} {self.model} engine stopped.")

    def honk(self):
        print(f"{self.brand} {self.model} honks: Beep Beep!")

class Car(Vehicle):
    def _init_(self, brand, model, fuel_type):
        super()._init_(brand, model)
        self.fuel = fuel  # BUG: 'fuel' is not defined

    def refuel(self, amount):
        print(f"Refueled {self.model} with {amount} liters of {self.fuel}.")
    
    def open_trunk(self):
        print(f"Trunk of {self.model} opened.")

class ElectricCar(Car):
    def _init_(self, brand, model, battery_capacity):
        super()._init_(brand, model, "Electric")
        self.battery_capacity = battery_capacity
    
    def charge_battery(self):
        print(f"{self.model} is charging. Battery at {self.battery_capacity} kWh.")

    def refuel(self, amount):  # BUG: Electric cars don't need refueling.
        print(f"{self.model} cannot be refueled with {amount} liters.")

# Creating objects
my_car = Car("Toyota", "Corolla", "Petrol")
my_car.start_engine()
my_car.refuel(20)  # BUG: Will cause an error due to incorrect attribute name.

my_electric_car = ElectricCar("Tesla", "Model S", 100)
my_electric_car.charge_battery()
my_electric_car.refuel(10)  # BUG: Electric car shouldn't refuel.

my_electric_car.open_trunk()
my_electric_car.honk()  # BUG: ElectricCar does not explicitly inherit honk method.