def rev(n):
    sum = 0
    reverse = 0
    while(n!=0):
        rem = n%10
        sum += rem
        reverse =reverse * 10+rem
        n = n//10
    return sum, reverse

if __name__=='__main__':
    n = int(input("Enter the number you want to reverse : "))
    s, reverse = rev(n)
    print(f'The reverse of the number is {reverse}')
    print(f'The sum of the digits of {n} is : {s}')
