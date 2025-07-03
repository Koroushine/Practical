from vpython import *

choice = 0
obj1 = None

while(choice != 7):
    print("Press 1 to display a Curve")
    print("Press 2 to display a Sphere")
    print("Press 3 to display a Cone")
    print("Press 4 to display an Arrow")
    print("Press 5 to display a Ring")
    print("Press 6 to display a Cylinder")
    print("Press 7 to exit")
    choice = int(input("Enter your choice: "))

    if obj1:
        obj1.visible = False  # hide previous object
        del obj1
        
    if choice == 1:
        curve_points = [vector(0,1,7), vector(-10, 3, 0), vector(5,-10,0), vector(10, 0, 2)]
        obj1 = curve(pos=curve_points, radius=0.1, color=color.orange)

    elif choice == 2:
        r = int(input("Enter the radius: "))
        obj1 = sphere(pos=vector(0,0,0), radius=r, color=color.green)

    elif choice == 3:
        r = int(input("Enter the radius: "))
        obj1 = cone(pos=vector(0,2,2), radius=r, color=color.yellow, thickness=0.7, axis=vector(0,0,2))

    elif choice == 4:
        obj1 = arrow(pos=vector(0,2,2), color=color.yellow, shaftwidth=1, axis=vector(4,0,0))

    elif choice == 5:
        r = int(input("Enter the radius: "))
        obj1 = ring(pos=vector(0,3,0), radius=r, color=color.green, thickness=0.7, axis=vector(0,1,0))

    elif choice == 6:
        r = int(input("Enter the radius: "))
        obj1 = cylinder(pos=vector(0,2,2), radius=r, color=color.orange, thickness=0.7, axis=vector(0,4,0))

    elif choice == 7:
        print("Exiting...")
    else:
        print("Invalid!")
