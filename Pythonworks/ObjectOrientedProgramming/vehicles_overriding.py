


class Parent:

    def vehicles(self):

        self.bikes=["passionpro","activa"]

        return self.bikes
    
   

class Child(Parent):

  def vehicles(self):
    self.bikes= super().vehicles()

    self.bikes.append("hunter")
     
    return self.bikes



  


tp=(10,)

print(type(tp))