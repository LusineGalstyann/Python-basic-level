class Car:

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def __str__(self):
        return f"\nMake: {self.make}\nModel: {self.model}\nYear: {self.year}\nColor: {self.color}"


# car1 = Car('Toyota', 'Camry', 2020, 'silver')
# print(car1)


class ElectricCar(Car):
    def __init__(self,make, model, year, color,kWh):
        super().__init__(make, model, year, color)
        self.kWh=kWh
    def __str__(self):
        parent=Car.__str__(self)
        return f"{parent}\nBattery size: {self.kWh}"

elcar1 = ElectricCar('Tesla', 'Model 3', 2022, 'red', 7500)
elcar2 = ElectricCar('Nissan', 'Leaf', 2021, 'green', 6000)

print(elcar1)
print(elcar2)