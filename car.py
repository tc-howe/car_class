import logging

logging.basicConfig(level=logging.ERROR, format='%(levelname)s: %(message)s')

# this class added just to test importing multiple classes from a single module
class EmptyExample:
    def __init__(self):
        pass


class Car:
    def __init__(self, make: str, model: str, year:int):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 5
        self.gas_level = 20
    
    def get_descriptive_name(self):
        long_name = f"{self.make} {self.model} {self.year}"

        return long_name.title()
    
    def get_odometer_reading(self):
        return self.odometer
    
    def update_odometer(self, reading: int):
        
        expected_type = int
        if not isinstance(reading, expected_type):
            logging.error(f"Type Mismatch: Expected {expected_type.__name__} for input, but got {type(reading).__name__} instead.")
            raise Exception("Input must be an integer value.")

        if reading >= self.odometer:
            self.odometer = reading
            print(f"Odometer reading updated to {self.odometer}.")
        else:
            raise Exception("Odometer reading must match or be greater than current value.")
    
    def increment_odometer(self, miles: int):
        
        # add error handling for int type check 

        if miles >= 0:
            self.odometer += miles
            print(f"Odometer reading updated to {self.odometer}.")
        else:
            raise Exception("Input must be 0 or greater.")
    
    def fill_gas_tank(self):
        print(f"Original gas level: {self.gas_level}")
        self.gas_level -= 5
        print(f"Current gas level: {self.gas_level}")
        print(f"Now filling tank")
        self.gas_level += 5
        print(f"Current gas level: {self.gas_level}")
    
