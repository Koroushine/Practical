def p16(oglst):
    cumulative_lst = []
    Sum = 0
    for i in oglst:
        Sum += i
        cumulative_lst.append(Sum)
    return cumulative_lst

def p17(lst):
    mul_lst = []
    for i in lst:
        intermediate = [i * j for j in range(1, 6)]
        mul_lst.append(intermediate)
    return mul_lst

def p18(strl):
    freq = {}
    strl = strl.lower()
    for i in strl:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

def p19(dict1):
    idict = {}
    for w,m in dict1.items():
        idict[m] = w
    return idict

if __name__ == '__main__':
    choice = 0  
    while choice != 5:
        print("---Menu---")
        print("1. Cumulative list")
        print("2. Multiple list")
        print("3. Frequency of letter")
        print("4. Dictionary of word inversion")
        print("5. Exit")
        print("-----------")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            print("Cumulative list")
            n = int(input("Enter the number of elements in the list: "))
            lst = []
            for i in range(n):
                a = int(input("Enter the element: "))
                lst.append(a)
            print("The cumulative list is:\n", p16(lst))

        elif choice == 2:
            print("Multiple list")
            n = int(input("Enter the number of elements in the list: "))
            lst = []
            for i in range(n):
                a = int(input("Enter the element: "))
                lst.append(a)
            print("The output of the list is:\n", p17(lst))

        elif choice == 3:
            print("Frequency of letter")
            strl = input("Enter your sentence: ")
            print("The corresponding frequency count is:\n", p18(strl))

        elif choice == 4:
            print("Word Meaning")
            d1 = {}
            for i in range(3):
                w = input("Enter the Word : ")
                m = input("Enter the meaning : ")
                if w not in d1:
                    d1[w] = m
            print("The original dictionary is \n", d1)
            print("The inverted dictionary is \n", p19(d1))
        elif choice == 5:
            print("Exiting the program...")

        else:
            print("Invalid choice! Please try again.")
