# Car  = [model, year, mileage, fuel_tank_capacity]

class Car:
    def __init__(self, model, year, mileage, fuel_tank_capacity):
        self.model=model
        self.year=year
        self.mileage=mileage
        self.fuel_tank_capacity=fuel_tank_capacity
        
    def __str__(self):
        car_str = ( '\n\nMODEL : ' + self.model + 
        '\nYEAR : ' + self.year + 
        '\nMILEAGE : ' + self.mileage + 
        '\nFUEL_TANK_CAPACITY : ' + self.fuel_tank_capacity)
        return car_str
        
car_a = Car("generic model no. 1", "2000", "1", "2")
print (car_a)

car_b = Car("generic model no. 2", "2001", "2", "4")
print (car_b)
