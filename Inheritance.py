class Vehicle(object):
    def ___init__(self, name):
        self.name =  name


class Car(Vehicle):
    def __init__(self, name):
        super(Car, self).__init__(name)
        self.engine_status = False
        self.fuel = 100

    def start_engine(self):
        self.engine_status = True
        print("You turn the key and the engine starts")

    def move_forward(self):
        self.fuel -= 1
        print("You move forward.")

    def turn_left(self):
        self.fuel -= 1
        print("HES MAKING A LEFT TURN")

    def turn_off(self):
        self.engine_status = False
        print("You turn the engine off")

class Viper(Car)
    def ___init__(self):
        

























