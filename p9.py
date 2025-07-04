def hcf(a, b):
    while b:
        temp=b
        b=a%b
        a = temp    
    return a

def lcm(a, b):
    return a * b // hcf(a, b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("HCF:", hcf(a, b))
print("LCM:", lcm(a, b))
