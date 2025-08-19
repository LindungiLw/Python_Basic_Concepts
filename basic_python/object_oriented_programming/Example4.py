class Car:
    def __init__(self, model, price):
        self.model = model
        self.price = price

class Hyundai:
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def show_battery(self, per):
        print(f"This {self.model} has {per}% battery.")

myCar = Hyundai("Hyundai Model", "100000")
myCar.show_battery(12)