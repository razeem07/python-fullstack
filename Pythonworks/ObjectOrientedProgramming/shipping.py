

class Shipping:


    def calculate_shipping_cost(self,weight):

        print(weight*5)


class ExpressShipping(Shipping):

    def calculate_shipping_cost(self, weight):
        print(weight*20)


class StandardShipping(Shipping):
    pass

    def calculate_shipping_cost(self, weight):
        
        print(weight*10)


expe_instance=ExpressShipping()

expe_instance.calculate_shipping_cost(10)

std_instance=StandardShipping()

std_instance.calculate_shipping_cost(10)

# polymorphism
    # method_overloading()

# class
# object
# __init__
# super()
# self
# inheritance
    #single
    #multilevel
    # multiple

# polymorphism
    #method_overloading

    # method_overriding

#Abstraction
    #hiding implimentation details



class Form:

    def is_valid(self):
        print("form class validate method")

    def clean(self):

        print("base form validation")

class EmployeeForm(Form):

    def clean(self):

        super().clean()

        print("employee form validation")

form_instance=EmployeeForm()

form_instance.is_valid()

form_instance.clean()
