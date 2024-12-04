# method_over_loading
# same method name different number of parameters
class Parent:

    def m1(self):
        print("parent m1 method")

    
class Child(Parent):

    def m1(self):
        print("child m1 method")
