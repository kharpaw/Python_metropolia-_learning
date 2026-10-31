import random
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_of_speed):
        new_speed = self.current_speed + change_of_speed

        if new_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed
        return self.current_speed

    def drive(self, number_of_hours):
        self.travelled_distance += self.current_speed * number_of_hours



class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed, battery_capacity):
        super().__init__(registration_number, maximum_speed)
        self.battery_capacity = battery_capacity
        
      
class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed, capacity):
        super().__init__(registration_number, maximum_speed)
        self.capacity = capacity
        

electric = ElectricCar("ABC-15", 180, 52.5)
gasoline = GasolineCar("ACD-123", 165, 32.3) 

speed1 = electric.accelerate(50)
speed2 = electric.accelerate(30)

electric.drive(3)
electric.drive(3)

print(speed1)
print(speed2)