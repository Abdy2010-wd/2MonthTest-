#OOП 2: Другие принципы ООП - Инкапсуляция, Полиморфизм.
class Car:
      def __init__(self, color, model):
       self.color = color
       self.speed = model

      def drive_to_location(self, location):
          print(f'Car {self.model} is driving to {location}')
class Bus(Car):
    def __init__(self, color, model, number):
        super().__init__(color, model)
        self.number = number

bus_40 = Bus('red', 'Mersedes Benz')
bus_40.drive_to_location(location=('Bishkek'))


