class Animale:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleeping(self):
        print(f"{self.name} is sleeping")

class Dog(Animale):
    def speak(slef):
        print("woof")

class Cat(Animale):
    def speak(slef):
            print("meaow")

class Mouse(Animale):
    def speak(slef):
            print("squeek")

dog = Dog("Scooby")
cat = Cat("Tom")
mouse = Mouse("Jerry")

print(dog.name)
print(dog.is_alive)

dog.eat()
dog.sleeping()
dog.speak()