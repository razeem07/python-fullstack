

from abc import ABC,abstractmethod

class Bike(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod  
    def accelerate(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

class Hunter(Bike):

    def start(self):
        print("hunter start method")

    def accelerate(self):
        print("hunter accelerate method")

    def stop(self):

        print("hunter stop")

hunter_instance=Hunter()

hunter_instance.start()