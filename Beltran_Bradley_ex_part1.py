# Starter code for part 1 exercises
# rename to lastname_firstname_ex_part1.py

import numpy as np

class circle:
    def __init__(self,radius=1):
        self.radius = radius

    def area(self):
        return np.pi*(self.radius**2)

    def perimeter(self):
        return np.pi*2*self.radius

def multiples(x,n):
    Z = []
    for i in range(n):
            Z.append(x*(i+1)) 
    return Z
#O(n*2)
def sum_positive(a):
    count = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i,j]>0:
                count += a[i,j]
    return count
#O(n)
def items_before(L,x):
    Z=[]
    for i in range(len(L)):
        if L[i] == x:
            break
        else:
            Z.append(L[i])
    return Z
#O(n)
def inverse_diagonal(a):
    Z=np.zeros(len(a))
    for i in range(len(a)):
        Z[i]=a[i,len(a)-i-1]
    return Z
#O(1)
def swap_halves(L1,L2):
    mid1 = len(L1)//2
    mid2 = len(L2)//2
    return L1[:mid1]+L2[mid2:], L2[:mid1]+L1[mid2:]
#O(n*2)
def subtract_row(a,r):
    ar = np.copy(a[r])
    for i in range(len(a)):
        for j in range(len(a[0])):
        
              a[i,j]=a[i,j]-ar[j]
    return a


if __name__ == "__main__":
    np.random.seed(1)

    print('Question 1')

    circle1 = circle()
    print('area:',circle1.area())
    print('perimeter:',circle1.perimeter())

    circle2 = circle(5)
    print('area:',circle2.area())
    print('perimeter:',circle2.perimeter())

    print('Question 2')
    print(multiples(3,5))
    print(multiples(5,10))

    print('Question 3')
    a1 = np.random.randint(-2,3,(2,4))
    a2 = np.random.randint(-3,6,(3,5))
    print(a1)
    print(a2)
    print(sum_positive(a1))
    print(sum_positive(a2))

    L1 = [6, 4, 8, 9, 1, 3, 7, 5, 2, 0]
    L2 = [18, 0, 12, 9, 6, 15, 3, 4]

    print('Question 4')
    print(items_before(L1,7))
    print(items_before(L1,6))
    print(items_before(L1,10))
    print(items_before(L2,15))
    print(items_before(L2,12))
    print(items_before([],12))

    print('Question 5')
    a1 = np.arange(16).reshape(4,4)*10
    a2 = np.arange(25).reshape(5,5)*5
    print(a1)
    print(a2)
    print(inverse_diagonal(a1))
    print(inverse_diagonal(a2))

    print('Question 6')
    L1 = [6, 4, 8, 9, 1, 3, 7, 5, 2, 0]
    L2 = [18, 0, 12, 9, 6, 15, 3, 4]
    L3 = [0 for i in range(6)]
    L4 = [1 for i in range(8)]
    La, Lb = swap_halves(L1,L2)
    print(La,Lb)
    La, Lb = swap_halves(L3,L4)
    print(La,Lb)

    print('Question 7')
    a1 = np.random.randint(0,10,(5,6))
    a2 = np.random.randint(0,10,(4,8))

    print(a1)
    subtract_row(a1,0)
    print(a1)

    print(a2)
    subtract_row(a2,2)
    print(a2)

'''
Expected results:
Question 1
area: 3.141592653589793
perimeter: 6.283185307179586
area: 78.53981633974483
perimeter: 31.41592653589793
Question 2
[3, 6, 9, 12, 15]
[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
Question 3
[[ 1  2 -2 -1]
 [ 1 -2 -2 -1]]
[[ 4  3 -1  1  2]
 [-1  1 -1  1  4]
 [ 4 -2  4 -3  3]]
4
27
Question 4
[6, 4, 8, 9, 1, 3]
[]
[6, 4, 8, 9, 1, 3, 7, 5, 2, 0]
[18, 0, 12, 9, 6]
[18, 0]
[]
Question 5
[[  0  10  20  30]
 [ 40  50  60  70]
 [ 80  90 100 110]
 [120 130 140 150]]
[[  0   5  10  15  20]
 [ 25  30  35  40  45]
 [ 50  55  60  65  70]
 [ 75  80  85  90  95]
 [100 105 110 115 120]]
[ 30  60  90 120]
[ 20  40  60  80 100]
Question 6
[6, 4, 8, 9, 1, 6, 15, 3, 4] [18, 0, 12, 9, 3, 7, 5, 2, 0]
[0, 0, 0, 1, 1, 1, 1] [1, 1, 1, 1, 0, 0, 0]
Question 7
[[9 9 7 6 9 1]
 [0 1 8 8 3 9]
 [8 7 3 6 5 1]
 [9 3 4 8 1 4]
 [0 3 9 2 0 4]]
[[ 0  0  0  0  0  0]
 [-9 -8  1  2 -6  8]
 [-1 -2 -4  0 -4  0]
 [ 0 -6 -3  2 -8  3]
 [-9 -6  2 -4 -9  3]]
[[9 2 7 7 9 8 6 9]
 [3 7 7 4 5 9 3 6]
 [8 0 2 7 7 9 7 3]
 [0 8 7 7 1 1 3 0]]
[[ 1  2  5  0  2 -1 -1  6]
 [-5  7  5 -3 -2  0 -4  3]
 [ 0  0  0  0  0  0  0  0]
 [-8  8  5  0 -6 -8 -4 -3]]
'''