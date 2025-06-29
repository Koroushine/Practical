def fac(num):
    if num==0:
        return 1
    else:
        f = 1
        for i in range(1,num+1):
            f *= i
        return f
num = int(input("Enter a number: "))
print("Factorial of", num, "is", fac(num))