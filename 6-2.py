class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return "Марка: {}, модель: {}".format(self.make, self.model)


class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        return "Марка: {}, модель: {}, тип топлива: {}".format(self.make, self.model, self.fuel_type)


car1 = Vehicle("audi", "a5")
car2 = Car("bmw", "m5", "gas")
print(car1.get_info())
print(car2.get_info())