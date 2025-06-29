def p(num):
    flag = True
    if num<2:
        flag = False
    else:  
        for i in range(2,num):
            if num%i==0:
                flag = False
                break
    if flag == False:
        print("Not prime!")
    else:
        print("Prime!")
    return flag

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(p(num))