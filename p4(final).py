import math
def area (side1, side2, side3) ->float:
    s:float = (side1+side2+side3)/2

    a=s-side1
    b=s-side2
    c=s-side3

    ar:float=math.sqrt(s*a*b*c)
    return ar

if __name__=='__main__':
    side1, side2, side3 = input("Enter the side separated with commas : ").split(',')

    side1 = float(side1)
    side2 = float(side2)
    side3 = float(side3)

    assert((side1+side2>side3)and (side2+side3>side1) and (side1+side3>side2))
    ar=area(side1,side2,side3)
    print(f'The area of the triangle is {ar}')