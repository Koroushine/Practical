l = input("Enter the numbers for the list : ")
l = l.split()
list = []
for i in l:
    list.append(int(i))

print(list)
counted = []
for i in list:
    if i not in counted:
        no = 0
        for j in list:
            if i == j:
                no += 1
        print(f"\n{i} : {no}")
        counted.append(i)
