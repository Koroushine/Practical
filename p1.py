choice = 1
while choice !=5:
    print("---Menu---")
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        a = int(input("a = "))
        b = int(input("b = "))
        c = a + b
        print(c)
    elif choice == 2:
        a = int(input("a = "))
        b = int(input("b = "))
        c = a - b
        print(c)
    elif choice == 3:
        a = int(input("a = "))
        b = int(input("b = "))
        c = a * b
        print(c)
    elif choice == 4:
        a = int(input("a = "))
        b = int(input("b = "))
        c = a / b
        print(c)
    elif choice == 5:
        print("Exiting...")
    else:
        print("Invalid Input!")