class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
        self.fiend = False


    def drive_to_location(self, location):
        print(f"Car {self.model} is diring to {location} ")

    def _last_car(self):
        print(f"test car [{self.model}")


car_honda = Car("black", "HONDA civit")
# car_honda._test_car()