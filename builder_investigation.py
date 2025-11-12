

class Car:

    def __init__(self, make, model, year, colour, engine_size):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour
        self.engine_size = engine_size

    def __str__(self):
        return f"{self.make} {self.model} {self.year} {self.colour} {self.engine_size}"


car = Car("Nissan", "Almera", 2012, "red", 1400)
print (car)

# alternative - create a CarBuilder class

class CarBuilder:
    def __init__(self):
        self._make = ""
        self._model = ""
        self._year = 2025
        self._colour = "red"
        self._engine_size = 1000

    def make(self, make):
        self._make = make
        return self

    def model(self, model):
        self._model = model
        return self
    
    def year(self, year):
        self._year = year
        return self

    def colour(self, colour):
        self._colour = colour
        return self

    def engine_size(self, engine_size):
        self._engine_size = engine_size
        return self
    
    def build(self):
        # lots of code to validate the options
        # TBD ...
        return Car(self._make, self._model, self._year, self._colour, self._engine_size)

cb = CarBuilder()

cb.make("Nissan") \
  .model("Micra") \
  .year(2012) \
  .colour("red") \
  .engine_size(1200)

car = cb.build()

print (car)


car2 = CarBuilder() \
  .make("Nissan") \
  .model("Micra") \
  .year(2012) \
  .colour("red") \
  .engine_size(1200) \
  .build()

print (car2)










