# polymorphism(more than one form)
#  method_overloading
#  method_overriding


# method_overloading(same method name and different number of parameters)
class Operations:


    def add(self,*args):

        print(sum(args))



obj=Operations()

obj.add(10,20,30)


obj.add(10,20)#error







