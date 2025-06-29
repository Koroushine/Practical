def fac(num):
    fact = 1
    for i in range(1, num+1):
        fact*=i
    return fact
def fib(num):
    a = 0
    b = 1
    lst1 = []

    if num == 1:
        lst1.append(a)
    else:
        lst1.append(a)
        lst1.append(b)
        for i in range(2,num):
            c = a+b
            lst1.append(c)
            a = b
            b = c
        return lst1
def dig(num):
    num = int(num)
    digit = int(num)
    return digit
def sum(num):
    digit = 0
    while(num!=0):
        digit+=num%10
        num = num/10
        digit = int(digit)
    return digit
if __name__=="__main__":
    print("Functions : ")
    print("1. Factorial")
    print("2. nth terms of fibonacci sequence")
    print("3. reverse")
    print("4. Sum")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        num = int(input("Enter your no. : "))
        fac(num)
        print(f'The factorial of {num} is {fac(num)}')
    elif choice == 2:
        num = int(input("Enter your term : "))
        print(f'The {num}th term of the fibonacci sequence is {fib(num)}')
    elif choice == 3:
        num = input ("Enter your number : ")
        print (f'The reverse of the digit {num} is {dig(num)}')
    elif choice == 4:
        num = int(input("Enter your number : "))
        print(f'The sum of {num} is {sum(num)}')
    