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
        

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars
             
    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-5,15)
            car.accelerate(speed_change)
            car.drive(1)
    def print_status(self):
        print("\nRegistration\tMax Speed\tCurrent Speed\tDistance")
        print("-" * 85)
        for car in self.cars:
                print(f"{car.registration_number}\t\t{car.maximum_speed}\t\t{car.current_speed}\t\t{car.travelled_distance}")
        print("-" * 85)
    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False

cars = []

for i in range(1,11):
    car = Car(f"ABC-{i}", random.randint(100,200))
    cars.append(car)
    
race = Race("Grand Demolition Derby", 8000, cars)

hours = 0

while not race.race_finished():
    race.hour_passes()
    hours += 1
    
    if hours % 10 == 0:
        race.print_status()
        
print("race finished")
race.print_status()