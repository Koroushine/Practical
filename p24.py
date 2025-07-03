import matplotlib.pyplot as plt

def accept(n):
    lst = []
    for i in range(n):
        val = float(input(f"Enter value {i+1}: "))
        lst.append(val)
    return lst

if __name__ == "__main__":
    n = int(input("Enter the total number of data : "))
    lst1 = accept(n)
    print(lst1)
    plt.hist(lst1)
    plt.xlabel("Data")
    plt.ylabel("Frequency")
    plt.title("list of integers")
    plt.show()