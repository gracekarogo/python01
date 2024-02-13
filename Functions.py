# Inbuilt functions
number = max(89,70,23,45,123)
print(number)

x = min(59,45,923,0,5)
print(x)

z = pow(2,3)
print(z)

#User-define functions
def name():
    print("Grace")

name() # calling a function


def student():
    name = "vincent"
    age = 18
    course = "MIT"
    print(name , age , course )

student()

# parameters
def students(name, age,course):
    print(name, age, course)

students("vincent",18,"MIT" )
students("vincent",18,"MIT" )
students("vincent",18,"MIT" )

#User defined function called employees should display details of 5 employees
#fullname,age,gender,position,salary
def employees(fullname, age ,gender ,position ,salary):
    print(fullname ,age ,gender ,position ,salary)

employees("melvin anderson" , 26 , "male","manager",80000)
employees("Jackie miles" , 40 , "female","CEO",300000)
employees("Drake Stone" , 35 , "male","Secretary",50000)
employees("Summer Williams" , 45 , "female","Director",150000)
employees("tommy jake" , 30 , "male","Head of organisation",300000)
