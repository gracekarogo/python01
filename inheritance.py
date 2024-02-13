#parent class / super class /base class
class animal:
    def speak(self):
        print("animal is speaking")
#child class / sub class / derived class
class dog(animal):
    def bark(self):
        print("dog is barking")

class cat(dog):
    def meow(self):
        print("cat is meowing")
a = animal()
d = dog()
d.bark()
d.speak()

c = cat()
c.meow()
c.speak()