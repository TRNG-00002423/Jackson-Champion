class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an animal."
    
    class Dog(Animal):
        def speak(self):
            return f"{self.name} says Woof!"
    
    class Cat(Animal):
        def speak(self):
            return f"{self.name} says Meow!"

rex = Animal.Dog("Rex")
socks = Animal.Cat("Socks")

print(rex.speak())
print(socks.speak())