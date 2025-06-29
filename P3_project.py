import math

#decimal function
def decimal():
    print("\nDecimal function activated!")
    print("Which of the following task you would like to perform : ")
    print("1. Returning Absolute value (fabs)")
    print("2. Returning Integral value (trunc)")
    print("3. Returning Highest integral value possible (ceil)")
    print("4. Returning Lowest integral value possible (floor)")
    print("5. Returning the rounded value (round)")
    print("6. Returning the integral and the decimal value")
    print("7. Returning the remender after division of two numbers")
    
    option = int(input("Option : "))

    match option:
        case 1: 
            print("1. Returning Absolute value (fabs)")
            num = float(input('Enter your value : '))
            print(f'Absolute value = {math.fabs(num)}')
        case 2:
            print("2. Returning Integral value (trunc)")
            num = float(input('Enter your value : '))
            print(f'Integral value = {math.trunc(num)}')
        case 3:
            print("3. Returning Highest integral value possible (ceil)")
            num = float(input('Enter your value : '))
            print(f'Highest Integral value = {math.ceil(num)}')
        case 4:
            print("4. Returning Lowest integral value possible (floor)")
            num = float(input('Enter your value : '))
            print(f'Lowest Integral value = {math.floor(num)}')
        case 5:
            print("5. Returing the rounded value (round)")
            num = float(input('Enter your value : '))
            print(f'Rounded value = {round(num)}')
        case 6:
            print("6. Returing the integral and the decimal value")
            num = float(input('Enter your value : '))
            print(f'Integral and decimal value = {math.modf(num)}')
        case 7:
            print("7. Returning the remender after division of two numbers")
            num1 = float(input('Enter your dividend value : '))
            num2 = float(input('Enter your divisor value : '))
            print(f'Remainder of {num1} divided by {num2} = {math.fmod(num1,num2)}')
#Exponents and Logarithms Functions
def el():
    print("\nExponents and Logarithms function activated!")
    print("Which of the following tasks would you like to perform : ")
    print("1. Square root (sqrt)")
    print("2. Power function (pow)")
    print("3. Exponential (exp)")
    print("4. Logarithm base 10 (log10)")
    print("5. Logarithm base 2 (log2)")
    print("6. Logarithm with custom base (log)")

    option = int(input("Option : "))

    match option:
        case 1:
            print("1. Square root (sqrt)")
            num = float(input('Enter your value : '))
            print(f'Square root = {math.sqrt(num)}')

        case 2:
            print("2. Power function (pow)")
            base = float(input('Enter the base value : '))
            exponent = float(input('Enter the exponent value : '))
            print(f'Power result = {math.pow(base, exponent)}')

        case 3:
            print("3. Exponential (exp)")
            num = float(input('Enter your value : '))
            print(f'Exponential result = {math.exp(num)}')

        case 4:
            print("4. Logarithm base 10 (log10)")
            num = float(input('Enter your value : '))
            print(f'Log10 result = {math.log10(num)}')

        case 5:  
            print("5. Logarithm base 2 (log2)")
            num = float(input('Enter your value : '))
            print(f'Log2 result = {math.log2(num)}')

        case 6:
            print("6. Logarithm with custom base (log)")
            num = float(input('Enter your value : '))
            base = float(input('Enter the base : '))
            print(f'Log result = {math.log(num, base)}')

        case _:
            print("Invalid option!")

# Trigonometric function 
def tri():
    print("\nTrigonometric function activated!")
    print("Which of the following tasks would you like to perform : ")
    print("1. Convert Radians to Degrees")
    print("2. Convert Degrees to Radians")
    print("3. Sine (sin)")
    print("4. Cosine (cos)")
    print("5. Tangent (tan)")

    option = int(input("Option : "))

    match option:
        case 1:
            print("1. Convert Radians to Degrees")
            num = float(input('Enter your radian value : '))
            print(f'Degrees = {math.degrees(num)}')

        case 2:
            print("2. Convert Degrees to Radians")
            num = float(input('Enter your degree value : '))
            print(f'Radians = {math.radians(num)}')

        case 3:
            print("3. Sine (sin)")
            num = float(input('Enter angle in radians : '))
            print(f'Sine value = {math.sin(num)}')

        case 4:
            print("4. Cosine (cos)")
            num = float(input('Enter angle in radians : '))
            print(f'Cosine value = {math.cos(num)}')

        case 5:
            print("5. Tangent (tan)")
            num = float(input('Enter angle in radians : '))
            print(f'Tangent value = {math.tan(num)}')

        case _:
            print("Invalid option!")

#Algebric function
def al():
    print("\nAlgebraic function activated!")
    print("Which of the following tasks would you like to perform : ")
    print("1. Factorial")
    print("2. Greatest Common Divisor (gcd)")

    option = int(input("Option : "))

    match option:
        case 1:
            print("1. Factorial")
            num = int(input('Enter a non-negative integer : '))
            if num < 0:
                print("Factorial is not defined for negative numbers.")
            else:
                print(f'Factorial = {math.factorial(num)}')

        case 2:
            print("2. Greatest Common Divisor (gcd)")
            num1 = int(input('Enter first number : '))
            num2 = int(input('Enter second number : '))
            print(f'GCD = {math.gcd(num1, num2)}')

        case _:
            print("Invalid option!")

option = 0
while (option != 5):
    print("\nScientific Calculator\n")
    print("Choose the function you would like to use :")
    print("1. Decimal Function")
    print("2. Exponents and Logarithms")
    print("3. Trigonometric")
    print("4. Algebric Function")
    print("5. Exit")

    option = int(input("Option : "))
    if option == 1:
        decimal()
    elif option == 2:
        el()
    elif option == 3:
        tri()
    elif option == 4:
        al()
    elif option ==5:
        print("Thanks for using our calculator!")
    else:
        print("Invalid option")
