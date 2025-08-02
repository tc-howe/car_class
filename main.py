from car import Car, EmptyExample
from electric_car import ElectricCar as EC # alias example
import empty

# Example of importing whole module w/o specifying class name in import
my_empty_class = empty.Empty()

print(f"\n\nCombustion Car:")
my_car = Car("Maker", "Combustion", 2024)

print(my_car.get_descriptive_name())
print(f"Odometer: {my_car.get_odometer_reading()}")

#odo = int(input("Update odometer value: "))
#my_car.update_odometer(odo)
my_car.update_odometer(10)

print(f"Incrementing miles by 1000:")
my_car.increment_odometer(1000)

print(f"Gas tank method:")
my_car.fill_gas_tank()

print(f"\n\nElectric Car:")
my_electric_car = EC("Maker", "Electric", 2025, 65)
print(my_electric_car.get_descriptive_name())
print(f"Battery size: {my_electric_car.battery.get_battery_size()}")

print(f"Gas tank method:")
my_electric_car.fill_gas_tank()

print(f"Battery range: {my_electric_car.battery.get_battery_range()}")
