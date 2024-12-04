class Car:

    def __init__(self,name,brand,fuel_type):

        self.name=name

        self.brand=brand

        self.fuel_type=fuel_type

    def display(self):

        print(self.name,self.brand,self.fuel_type)

    def __str__(self):

        return self.name
  
car_instance1=Car("swift","suzuki","petrol")

car_instance1.display()

print(car_instance1)

# string representation of a object

# __str__(self)

# class Editor (name,vendor)
# editor_instance print => name