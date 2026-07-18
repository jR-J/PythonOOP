from abc import ABC, abstractmethod
class Vehicle:
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    
    def go(self):
         print("You drive the car")
            
    def stop(self):
         print("You stop the car")
        

class Motocycle(Vehicle):
        
    def go(self):
         print("You ride the moto..")
        
    
    def stop(self):
        print("you stop the moto..")


car = Car()
moto = Motocycle()

car.go()
car.stop()
        