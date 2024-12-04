

class SuperHero:

    def __init__(self,name,suit):

        self.name=name

        self.suit=suit

    def __str__(self):

        return self.name


class SpiderMan(SuperHero): 

    def __init__(self,name,suit):

        super().__init__(name,suit)


    def super_power(self):

        print("spider sense","web shooting","sticky hands")



class MinnalMurali(SuperHero):

    def __init__(self, name, suit):
        
        super().__init__(name,suit)

    def super_power(self):

        print("running","jumping","reflex")


minnal_murali_instance=MinnalMurali("minnamlmurali","minnalmurali suit")

print(minnal_murali_instance)

minnal_murali_instance.super_power()    
