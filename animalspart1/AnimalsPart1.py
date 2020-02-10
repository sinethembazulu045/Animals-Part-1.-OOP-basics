class Animal:
    def name(self):
        pass
    def sound(self):
        pass
    def eat(self):
        pass  
class Dog(Animal):
    def sound(self):
        print("Dog barks")
    def eat(self):
        print("Rax eats")
   

class Cat(Animal):
    def sound(self):
        print("Cat meows")
    def eat(self):
        print("Stormy eats")

dog = Dog()
cat =Cat()
cat.sound()
dog.sound()
dog.eat()
cat.eat()