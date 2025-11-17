def hello():
    print("Hello function")


hello()


def sum(a=10, b=90):
    return a+b


print(sum(20, 60))


def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i
    return fact


num = int(input("Enter number:= "))
print(factorial(num))
