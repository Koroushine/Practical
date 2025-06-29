n = int(input("Enter no. of rows: "))
for i in range(n):
    for j in range(i + 1, 2 * i + 2):
        print(j, end=" ")
    for j in range(2 * i, i, -1):
        print(j, end=" ")
    print()
