pi = 22/7

def cube():
    s = int(input("Enter the value of side: "))
    volume = s * s * s
    return print("Volume of Cube is: ", volume)

def cuboid():
    l = int(input("Enter the value of length: "))
    b = int(input("Enter the value of breadth: "))
    h = int(input("Enter the value of height: "))
    base_area = l * b
    volume = base_area * h
    return print("Volume of Cuboid is: ", volume)

def cylinder():
    r = int(input("Enter the value of radius: "))
    h = int(input("Enter the value of height: "))
    volume = pi * r * r * h
    return print("Volume of Cylinder is: ", volume)

