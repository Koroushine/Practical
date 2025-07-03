import matplotlib.pyplot as plt
def vs():
    a = []
    b = []
    num = int(input("Enter the no. of person : "))
    for i in range(num):
        x = input("Enter the name of the handsome : ")
        pulse = int(input(f"Enter the pulse rate of {x} : "))
        a.append(x)
        b.append(pulse)
    plt.plot(a,b, marker = 'd')
    plt.xlabel("Students")
    plt.ylabel("pulse rate")
    plt.title("Pulse rate vs height")
    plt.show()
if __name__ == "__main__":
    vs()