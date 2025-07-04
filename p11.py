import math
def sum_series(n,x):
    total = 1
    sign = -1
    series="1"

    for i in range(2,n+1,2):
        term = (x**i)/math.factorial(i)
        total += sign * term

        if sign == -1:
            series += f"-x^{i}/{i}!"
        else:
            series += f"+x^{i}/{i}!"
        sign*=-1
    print("Series : ", series)
    return total

if __name__=="__main__":
    x = float(input("Enter value of x : "))
    n = int(input("Enter max power(even number): "))

    if n%2!=0:
        print("Please enter an even number : ")
    else:
        result = sum_series(n,x)
        print("Sum of the series is : ", result)
    