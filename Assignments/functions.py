def demo(x):
    y = x + 3
    return y


print(demo(15))


def my_function(fname):
    print(fname + " Hignet")


my_function("Caroline")
my_function("Melvyn")
my_function("David")
my_function("Ann")

a = 3
b = 2
c = 1


def demo():
    y = (a + b + c)
    return y


demo()


def my_function():
    students = ["Caro", "Cecilia", "Pauline"]
    for s in students:
        print("The Azubi student is " + s)


my_function()


def area(radius):
    print(3.14 * (radius ** 2))


area(7)


def areaTriangle(base, height):
    return 1/2 * base * height


areaTriangle(2, 4)

def function_that_prints():
    print("I printed")

def function_that_returns():
    return "I returned"

f1 = function_that_prints()
f2 = function_that_returns()
print("Now let us see what the values of f1 and f2 are")
print(f1)
print(f2)
