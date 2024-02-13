try:
    print(x)
except:
    print("name error occurred")
finally:
    print("success")


num1 = 20
num2 = 0
try:
    print(num1 / num2)
except:
    print("zero division error occured")

# user defined function
try:
    def multiply(x, y):
        return x * y
except:
    print("exception occured")
finally:
    print("success")
print(multiply(10,20))

