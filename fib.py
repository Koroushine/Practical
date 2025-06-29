def fic(n):
    list = []
    a = 0
    b = 1

    if n == 1:
        list.append(a)
    else:
        list.append(a)
        list.append(b)
        for i in range(2,n):
            sum = a + b
            list.append(sum)
            a = b
            b = sum
    return list

if __name__=="__main__":
    n = int(input("Enter the number till which you want to have the fibonacci series : "))
    print(f'The fibonacci series till {n} is {fic(n)}')
