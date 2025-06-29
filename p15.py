import numpy as np

def inputmatrix(r:int,c:int):
    mat = []
    for i in range(r):
        row = input(f'Enter the {i+1}th row : ').split(',')
        mat.append([int(j) for j in row])
    return np.matrix(mat)
def add_compatible(mat1, mat2):
    if mat1.shape!=mat2.shape:
        return False
    else:
        return True
def mul_compatible(mat1,mat2):
    if mat1[1].shape!=mat2[0].shape:
        return False
    else:
        return True
    
def addmatrix(mat1,mat2):
    if(add_compatible(mat1,mat2)):
        return mat1+mat2
    else:
        return 'Matrices are not compatible to add'

def mulmatrix(mat1,mat2):
    if(mul_compatible(mat1,mat2)):
        return mat1*mat2
    else:
        return 'Matrices are not compatible to multiple'
    
if __name__=='__main__':
    r1 = int(input('Enter the numbers of rows for the first matrix : '))
    c1 = int(input('Enter the numbers of columns for the first matrix : '))
    mat1 = inputmatrix(r1,c1)
    print(mat1)
    
    r2 = int(input('Enter the numbers of rows for the second matrix : '))
    c2 = int(input('Enter the numbers of columns for the second matrix : '))
    mat2 = inputmatrix(r2,c2)
    print(mat2)
    print('Press 1 to add the matrices \n Press 2 to multiply the Matrices')
    choice = int(input("Enter your choice : "))
    if choice == 1:
        print('The sum of the matrices is : \n', addmatrix(mat1, mat2))
    elif choice == 2:
        print('The product of the matrices is : \n', mulmatrix(mat1, mat2))