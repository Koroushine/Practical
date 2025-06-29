def pattern():
    a = int(input("Enter the number of rows you want to print (odd number): "))

    # Upper half of the diamond
    for i in range(1, a + 1, 2): #1,3,5
        print(" " * ((a - i) // 2) + "*" * i)

    # Lower half of the diamond
    for i in range(a - 2, 0, -2):
        print(" " * ((a - i) // 2) + "*" * i)

if __name__=="__main__":
    pattern()

#   * 
#  ***
# *****
#  ***
#   *