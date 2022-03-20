pi = 22/7

def cube_surface():
    l = int(input("Enter the value of length: "))
    surfacearea = 6 * l * l
    return print("Surface Area of Cube is: ", surfacearea)

def cuboid_surface():
    l = int(input("Enter the value of length: "))
    b = int(input("Enter the value of breadth: "))
    h = int(input("Enter the value of height: "))
    surfacearea = 2 * (l*b + b*h + h*l)
    return print("Surface Area of Cuboloid is: ", surfacearea)

def cylinder_surface():
    r = int(input("Enter the value of radius: "))
    h = int(input("Enter the value of height: "))
    surfacearea = 2 * pi * r * (r + h)
    return print("Surface Area of Cylinder is: ", surfacearea)