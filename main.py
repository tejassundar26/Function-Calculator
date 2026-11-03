
a = float(input("Enter the first number"))
b = float(input("Enter the second number"))
try:
    def add(a , b):
        return a + b
    c = float(input("Enter the first number"))
    d = float(input("Enter the second number"))
    def subtract(c , d):
        return c - d
    e = float(input("Enter the first number"))
    f = float(input("Enter the second number"))
    def multiply(e , f):
        return e * f
    g = float(input("Enter the first number"))
    h = float(input("Enter the second number"))
    def divide(g , h):
        return g // h
except ValueError:
    print("Invalid Input!")
except ZeroDivisionError:
    print("Division by zero ")