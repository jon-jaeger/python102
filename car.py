#@title Car Class
class Car:
  def __init__(self, car_name, fuel_capacity, mileage, gas_level):
    self.carName = car_name
    self.fuelCapacity = fuel_capacity
    self.mileage = mileage
    self.gasLevel = gas_level

  # ✅ Fixed: added 'self' to all getter methods
  def get_CarName(self):
    return self.carName

  def get_FuelCapacity(self):
    return self.fuelCapacity

  def get_Mileage(self):
    return self.mileage

  def get_GasLevel(self):
    return self.gasLevel

  def __repr__(self):
    car_repr = (f'name: {self.carName} '
                f'capacity: {self.fuelCapacity} '
                f'mileage: {self.mileage} '
                f'gas_level: {self.gasLevel}')
    return car_repr

  def __str__(self):
    car_str = ('\nName: ' + self.carName +
               '\nFuel Capacity: ' + str(self.fuelCapacity) +
               '\nMileage: ' + str(self.mileage) +        # ✅ Fixed: typo "Milage" → "Mileage"
               '\nCurrent Gas Level: ' + str(self.gasLevel))
    return car_str

  def drive(self, distance):
    fuel_needed = distance / self.mileage
    if fuel_needed < self.gasLevel:
      self.gasLevel = self.gasLevel - fuel_needed
      print('\n', distance, 'miles travelled!')
    else:
      capable_distance = self.gasLevel * self.mileage
      self.gasLevel = 0
      print('\n', capable_distance, 'miles travelled!', distance - capable_distance, 'miles to go.')

  def fillGas(self, amount):
    amount_car_can_take = self.fuelCapacity - self.gasLevel

    if amount_car_can_take < amount:
      self.gasLevel = self.fuelCapacity
      print('\nGas tank is full now! You wasted', (amount - amount_car_can_take), 'out of', amount, 'gallons!')
    else:
      self.gasLevel += amount
      print(f'\n{amount} gallons added to the tank!')

  def can_drive(self, distance):
    capable_distance = self.gasLevel * self.mileage
    return capable_distance > distance


print("\nCreating Mom's Car")
moms_car = Car('Volvo', 50, 20, 50)
print(moms_car)

print("\nDrive mom's car for 100 miles")
moms_car.drive(100)
print(moms_car)

print("\nDrive mom's car for 1000 miles")
moms_car.drive(1000)
print(moms_car)

print("\nFilling in 30 gallons in Mom's car")
moms_car.fillGas(30)
print(moms_car)

print("\nFilling in 100 gallons in Mom's car")
moms_car.fillGas(100)
print(moms_car)