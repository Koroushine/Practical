# 2 = 1 x 2
# 3 = 1 X 2 X 3
def fac():
    a = int(input("Enter the number : "))
    pro = 1
    for i in range (1,a+1):
        pro *= i
    return pro

if __name__=="__main__":
    print("The factorial is :",fac())
