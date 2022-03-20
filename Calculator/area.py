pi = 22/7

def trapezium():
    h = int(input("Enter the value of height: "))
    a = int(input("Enter the value of side a: "))
    b = int(input("Enter the value of side b: "))
    area = 1/2*h*(a + b)
    return print("Area of Trapezium is: ", area)

def generalQuad():
    d = int(input("Enter the value of diagonal: "))
    h1 = int(input("Enter the value of height 1: "))
    h2 = int(input("Enter the value of height 2: "))
    area = 1/2*d*(h1+h2)
    return print("Area of General Quadrilateral is: ", area)

def rhombus():
    d1 = int(input("Enter the value of diagonal 1: "))
    d2 = int(input("Enter the value of diagonal 2: "))
    area = 1/2*d1*d2
    return print("Area of Rhombus is: ", area)

def circle():
    r = int(input("Enter the value of radius: "))
    area = pi*r*r
    return print("Area of Circle is: ", area)

def parallelogram():
    b = int(input("Enter the value of base: "))
    h = int(input("Enter the value of height: "))
    area = b * h
    return print("Area of Parallelogra is: ", area)

def triangle():
    b = int(input("Enter the value of base: "))
    h = int(input("Enter the value of height: "))
    area = 1/2*b*h
    return print("Area of Triangle is: ", area)

def square():
    a = int(input("Enter the value of side: "))
    area = a * a
    return print("Area of Square is: ", area)

def rectangle():
    l = int(input("Enter the value of length: "))
    b = int(input("Enter the value "))
    area = l * b
    return print("Area of Rectangle is: ", area)


