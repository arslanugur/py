# SECTION 1
# Inheritance provides a way to share functionality between classes.
# Imagine several classes, Cat, Dog, Rabbit and so on. 
# Although they may differ in some ways (only Dog might have the method bark), they are likely to be similar in others (all having the attributes color and name).
# This similarity can be expressed by making them all inherit from a superclass Animal, which contains the shared functionality.
# To inherit a class from another class, put the superclass name in parentheses after the class name.
# Example: 
class Animal: 
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Cat(Animal):
    def purr(self):
        print("Purr...")
        
class Dog(Animal):
    def bark(self):
        print("Woof!")

fido = Dog("Fido", "brown")
print(fido.color)
fido.bark()


comments


