class Person:
    def __init__(self,firstname,age,gender):
        self.firstname=firstname
        self.age = age
        self.gender = gender
    def details(self):
        print(self.firstname,"is studying")

teacher = Person("Joe",34,"male")
Accountant= Person("Arsha",30,"female")
Doctor = Person("John",45,"male")
print(teacher.firstname,teacher.age,teacher.gender)
print(Accountant.firstname,Accountant.age,Accountant.gender)