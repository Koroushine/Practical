def pattern(n):
    j = n//2
    m = n    
    for l in range(1, n+1,2):
        print(" "*((n-l)//2)+"*"*l)

    for i in range(n-2, 0,-2):
        print(" "*((n-i)//2)+"*"*i)

if __name__=="__main__":
    n = int(input("Enter the no. of rows : "))
    pattern(n)