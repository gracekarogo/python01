#Data Type
number = 45 # int
bun = 56.78 # float
greeting = "Hello there" # str
isPythonInteresting = True # bool


# variable storing multiple values
languages = ["python" , "PHP" , "java"] # List
fruits = ("apple" , "banana" , "pineapple") # Tuple
countries = {"Kenya" , "China" , "USA"} #Set
#Dictionary
details = {
    "firstname" : "Grace",
    "Age" : 17,
    "course" : "MIT",
    "Nationlity" : "North America"
}


print(number)
print(greeting)
print(countries)
print(isPythonInteresting)
print(details ["course"])
print(details ["Nationlity"])
print(details)

# Determining the data type
print(type(details))
print((type)(countries))


# type casting - converting one data type to another
print(float(number))
print(int(bun))
