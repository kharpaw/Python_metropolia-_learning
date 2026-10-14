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
        

                

car = Car("ABC-123", 142)

car.current_speed = 60
car.travelled_distance = 2000

car.drive(1.5)

print("Travelled distance:", car.travelled_distance, "km")


