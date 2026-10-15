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

    def drive(self, number_of_hours):
        self.travelled_distance += self.current_speed * number_of_hours


cars = []

for i in range(1, 11):
    maximum_speed = random.randint(100, 200)
    registration_number = "ABC-" + str(i)

    car = Car(registration_number, maximum_speed)
    cars.append(car)

race_finished = False

while not race_finished:


    for car in cars:
        change = random.randint(-10, 15)
        car.accelerate(change)
        car.drive(1)

       
        for car in cars:
            if car.travelled_distance >= 10000:
                race_finished = True
                break


       
print(f"{'Registration':<15}{'Max speed':<15}"
f"{'Current speed':<18}{'Distance (km)':<15}")

print("-" * 63)

for car in cars:
    print(f"{car.registration_number:<15}"
    f"{car.maximum_speed:<15}"
    f"{car.current_speed:<18}"
    f"{car.travelled_distance:<15.1f}")


