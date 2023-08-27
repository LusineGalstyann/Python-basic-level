class Car:

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def __str__(self):
        return f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}\nColor: {self.color}"


car1 = Car('Toyota', 'Camry', 2020, 'silver')
print(car1)
