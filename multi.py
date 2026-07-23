class Animale:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animale):
    def flee(self):
        print(f"{self.name} is fleeing")

# multiple inheritance - Inheriting from more than one parent class
# multilevel           - inherit from a parent that inherits from another parent
class Predator(Animale):
    def hunt(self):
        print(f"{self.name} is hunting")


class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


class Fish(Prey, Predator): #multiple inh
    pass

rabbit = Rabbit("buggs")
hawk = Hawk("Bold")
fish = Fish("Nemo")

rabbit.flee()
rabbit.eat()
rabbit.sleep()

hawk.hunt()
hawk.eat()
hawk.sleep()

fish.hunt()
fish.flee()
fish.eat()
fish.sleep()

