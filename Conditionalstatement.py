temperature = 13
if temperature > 25:
    print("It is hot")
else:
    print("It is cold")

    #A program that returns the largest number among three numbers
    num1 = 45
    num2 = 56
    num3 = 21
    if num1 > num2 and num1 > num3:
        print(num1, "is the largest number")
    elif num2 > num1 and num2 > num3:
        print(num2, "is the largest number")
    else:
        print(num3, "is the largest number")
    # A program that checks whether a number is even or odd
number = 45
if number % 2 == 0:
    print(number, "is even")
else:
    print("numberis odd")

    #Assignment
    # A program that checks whether a number is prime
    def is_prime (number):
        if number <= 1:
            return False
        for i in range (2  , int(number **0.5)):
            if number % i == 0:
                return False
        return True
    print((is_prime)(1))
    print(is_prime(17))



