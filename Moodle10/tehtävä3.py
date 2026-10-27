
class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom

    def floor_up(self):
        if self.current < self.top:
            self.current += 1
            print(f"Elevator is now on floor {self.current}")

    def floor_down(self):
        if self.current > self.bottom:
            self.current -= 1
            print(f"Elevator is now on floor {self.current}")

    def go_to_floor(self, floor):
        if floor < self.bottom or floor > self.top:
            print("Invalid floor")
            return

        while self.current < floor:
            self.floor_up()

            while self.current > floor:
                self.floor_down()


class Building:
    def __init__(self, bottom, top, num_of_elevators):
        self.top = top
        self.bottom = bottom
        self.num_of_elevators = num_of_elevators
        self.elevators = []

        for i in range(num_of_elevators):
            self.elevators.append(Elevator(bottom, top))

    def run_elevator(self, elevator_number, destinations):
        self.elevators[elevator_number-1].go_to_floor(destinations)
        
    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom)
        



building = Building(1, 13, 4)
building.run_elevator(1, 10)
building.run_elevator(1,5)
building.run_elevator(3,5)
building.run_elevator(4,10)

building.fire_alarm()




