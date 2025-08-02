from car import Car


class ElectricCar(Car):
    def __init__(self, make: str, model: str, year:int, capacity: int):
        super().__init__(make, model, year)
        self.battery = Battery(capacity)
    
    def fill_gas_tank(self):
        """Overrides the method from the parent class"""

        print(f"Electric cars do not have gas tanks.")


class Battery():
    def __init__(self, battery_size=40):
        self.battery_size = battery_size
    
    def get_battery_size(self):
        return self.battery_size
    
    def get_battery_range(self):
        if self.battery_size <= 40:
            range = 150
        else:
            range = 250
        
        return range