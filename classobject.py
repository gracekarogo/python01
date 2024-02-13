# Class is a blueprint of an object
#object is an instance of a class
class person:
    # properties / attributes / characteristics
    age = 23
    name = "Bill"

    def talk(self):
        # Method /Function /Behaviour
        print("person is talking")

teacher = person()
print(teacher.name)
print(teacher.age)

teacher.talk()