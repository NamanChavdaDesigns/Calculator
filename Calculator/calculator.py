from area import *
from volume import *
from surface_area import *

print("This is a calculator to calculate Surface Area, Area and Volume.")
print("Enter your choice,")
choice = int(input("Type 1 for Surface Area, 2 for Area and 3 for Volume: "))

if choice == 1:
    print("Enter your shape,")
    shape_surfacearea = int(
        input("Type 1 for Cube, 2 for Cuboid and 3 for Cylinder: "))
    if shape_surfacearea == 1:
        cube_surface()
    elif shape_surfacearea == 2:
        cuboid_surface()
    elif shape_surfacearea == 3:
        cylinder_surface()
    else:
        print("Please choose a valid shape :(")

elif choice == 2:
    print("Enter your shape,")
    shape_area = int(input('''Type 1 : Trapezium
     2 : General Quadrilateral
     3 : Rhombus
     4 : Circle
     5 : Parallelogram
     6 : Triangle
     7 : Square
     8 : Recatngle : '''))

    if shape_area == 1:
        trapezium()
    elif shape_area == 2:
        generalQuad()
    elif shape_area == 3:
        rhombus()
    elif shape_area == 4:
        circle()
    elif shape_area == 5:
        parallelogram()
    elif shape_area == 6:
        triangle()
    elif shape_area == 7:
        square()
    elif shape_area == 8:
        rectangle()
    else:
        print("Please choose a valid shape :(")

elif choice == 3:
    print("Enter your shape,")
    shape_volume = int(
        input("Type 1 for Cube, 2 for Cuboid and 3 for Cylinder."))

    if shape_volume == 1:
        cube()
    elif shape_volume == 2:
        cuboid()
    elif shape_volume == 3:
        cylinder()
    else:
        print("Please choose a valid shape :(")

print("Hope you enjoyed calculating \nhave fun :)")
print("GitHub : https://github.com/NamanChavdaDesigns/NamanChavdaDesigns")
