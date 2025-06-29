import math 
def area()->float:
    side1, side2, side3 = input("Enter the side separated with commas:").split(',')

    side1 = float(side1)
    side2 = float(side2)
    side3 = float(side3)

    if ((side1 + side2> side3) and (side2 + side3>side1) and (side3+side1 > side2)):
        s=(side1+side2+side3)/2

        a = s-side1
        b = s-side2
        c = s-side3

        ar = math.sqrt(s*a*b*c)
        return ar
    else:
        print("Invalid triangle!")

if __name__=="__main__":
    ar = area()
    print(f'The area of the triangle is {ar}')
    