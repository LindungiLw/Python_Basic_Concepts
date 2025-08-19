class Car:
    def __init__(self, model, price):
        self.model = model
        self.price = price

class AutoDriving:

    def check(self):
        print("Auto driving is enabled")

class Hyundai(Car, AutoDriving):
    def __init__(self, model, price, color):
        super().__init__(model, price)
        self.color = color

    def show_battery(self, per):
        print(f"This {self.model} has {per}% battery.")

c1 = Hyundai("Hyundai Model", "1000000000", "Blue")
c1.check()
c1.show_battery(12)