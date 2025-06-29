#Write a function to return the LCM and HCF of two numbers.

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def lcm_hcf(num1, num2):
    a = num1
    b = num2
    while b! = 0:
        a = b
        b = a % b
        hef = a
        lcm = (num1 * num2)
    return lcm, hef

if __name__ == "__main__":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if is_prime(num1):
        print 