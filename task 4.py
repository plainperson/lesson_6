class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f'Новая машина: {self.name} цвет: {self.color} полиция? {self.is_police}')


    def go(self):
            print(f'машина {self.name} поехала')

    def stop(self):
            print(f'машина {self.name} остановилась')

    def turn(self, direction):
            print(f'машина {self.name} повернула {"налево" if direction == 0 else "направо"}')

class TownCar(Car):
    def show_speed(self):
        print(f'машина {self.name} едет со скоростью {self.speed} {"Скорость превышена!" if self.speed > 60 else "Скорость в норме"}')

class WorkCar(Car):
    def show_speed(self):
        print(f'машина {self.name} едет со скоростью {self.speed} {"Скорость превышена!" if self.speed > 40 else "Скорость в норме"}')

class SportCar(Car):
    pass

class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


car_1 = TownCar('taxi', 'white', 45)
car_1.turn(1)
car_1.show_speed()


