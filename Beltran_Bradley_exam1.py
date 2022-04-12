# Please rename as lastname_firstname_exam1.py
import numpy as np
from numpy.core.fromnumeric import size

class circle:
    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return (self.radius**2)*np.pi

    def perimeter(self):
        return self.radius*2*np.pi
    
    def diameter(self):
        return self.radius*2
    
    def increase_radius(self,f=2):
        self.f=f
        if self.f < 1:
            return self.radius
        return self.radius*self.f 
    
def nn(n):
    # T(n) = O(n)
    L = []
    for i in range(n):
        L.append(n)
    return L  

def same_index_and_value(A):
    # T(n) = O(n)
    count = 0
    L=[]
    for i in range(len(A)):
        if A[i]==i:
            count+=1
            L.append(A[i])
    A1=np.zeros(count)
    for i in range(len(L)):
            A1[i]=L[i]
    return A1
               
def less_than_k(L,k):
    # T(n) = O(n)
    L1=[]
    for i in range(len(L)):
        if L[i]<k:
            L1.append(L[i])
    return L1

def rows_with_negative_values(A):
    # T(r,c) = O(n*c)
    count = 0
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i,j]<0:
                A[i]=0
                count=count+1

            
    return count  

def sum_prev(L):
    # T(n) = O(n)
    Ls = []
    current = 0
    for i in range(len(L)):
        current = L[i]+current
        Ls.append(current)
    return Ls  

def sum_edge(A):
    # T(r,c) = O(n*c)
    sum = 0
    for i in range(len(A)):
        for j in range(len(A[i])):
            if i == 0 or i == len(A)-1:
                sum += A[i,j]
        if i == 0 or i == len(A)-1:
            sum+=0
        else:
            sum += A[i,0] + A[i,len(A)]
    return sum
        
if __name__ == "__main__":

    print('Question 1')
    
    circle1 = circle()
    print('radius:',circle1.radius)
    print('area:',circle1.area())
    print('perimeter:',circle1.perimeter())
    print('diameter:',circle1.diameter())
    print('--------------')
    circle1.increase_radius()
    print('radius:',circle1.radius)
    print('area:',circle1.area())
    print('perimeter:',circle1.perimeter())
    print('diameter:',circle1.diameter())
    print('--------------')
    circle1.increase_radius(0.5)
    print('radius:',circle1.radius)
    print('area:',circle1.area())
    print('perimeter:',circle1.perimeter())
    print('diameter:',circle1.diameter())
    print('--------------')
    circle1 = circle(10)
    print('radius:',circle1.radius)
    print('area:',circle1.area())
    print('perimeter:',circle1.perimeter())
    print('diameter:',circle1.diameter())
    print()
   
    print('Question 2')
    for i in range(0,10):
        print(i,nn(i))
        print('--------------')
    
    print('Question 3')
    np.random.seed(3)
    for i in range(4,10):
        A = np.random.permutation(i)
        print(A)
        print(same_index_and_value(A))  
        print('--------------')
    
    print('Question 4')
    np.random.seed(44)
    L = list(np.random.randint(0,10,size=11))
    print(L)
    for k in range(1,11):
        print(k, less_than_k(L,k))
   
    print('Question 5')
    np.random.seed(5)
    for i in range(4,7):
        A = np.random.randint(-2,9,size=(i,4))
        print(A)
        print(rows_with_negative_values(A))  
        print('--------------')
        
    print('Question 6')
    np.random.seed(6)
    for i in range(3):
        L = list(np.random.randint(0,5,size=10))
        print(L)
        print(sum_prev(L))
        print('--------------')
        
    print('Question 7')
    np.random.seed(7)
    for i in range(2,5):
        A = np.random.randint(1,5,size=(i,i+1))
        print(A)
        print(sum_edge(A))    
        print('--------------')
        
'''
Question 1
radius: 1
area: 3.141592653589793
perimeter: 6.283185307179586
diameter: 2
--------------
radius: 2
area: 12.566370614359172
perimeter: 12.566370614359172
diameter: 4
--------------
radius: 2
area: 12.566370614359172
perimeter: 12.566370614359172
diameter: 4
--------------
radius: 10
area: 314.1592653589793
perimeter: 62.83185307179586
diameter: 20

Question 2
0 []
--------------
1 [1]
--------------
2 [2, 2]
--------------
3 [3, 3, 3]
--------------
4 [4, 4, 4, 4]
--------------
5 [5, 5, 5, 5, 5]
--------------
6 [6, 6, 6, 6, 6, 6]
--------------
7 [7, 7, 7, 7, 7, 7, 7]
--------------
8 [8, 8, 8, 8, 8, 8, 8, 8]
--------------
9 [9, 9, 9, 9, 9, 9, 9, 9, 9]
--------------
Question 3
[3 1 0 2]
[1]
--------------
[1 2 4 0 3]
[]
--------------
[0 4 1 2 3 5]
[0 5]
--------------
[6 1 3 4 0 5 2]
[1 5]
--------------
[3 5 4 1 2 0 6 7]
[6 7]
--------------
[6 0 5 7 3 1 4 8 2]
[]
--------------
Question 4
[4, 3, 1, 3, 0, 4, 3, 8, 7, 7, 6]
1 [0]
2 [1, 0]
3 [1, 0]
4 [3, 1, 3, 0, 3]
5 [4, 3, 1, 3, 0, 4, 3]
6 [4, 3, 1, 3, 0, 4, 3]
7 [4, 3, 1, 3, 0, 4, 3, 6]
8 [4, 3, 1, 3, 0, 4, 3, 7, 7, 6]
9 [4, 3, 1, 3, 0, 4, 3, 8, 7, 7, 6]
10 [4, 3, 1, 3, 0, 4, 3, 8, 7, 7, 6]
Question 5
[[ 1  4  4 -2]
 [ 7  6  2  5]
 [-2 -2  5 -1]
 [ 3  5 -2 -1]]
3
--------------
[[ 2  4  0  7]
 [ 7  8  7  7]
 [-1  0  5 -2]
 [ 3  8 -2 -2]
 [ 2  2  7  1]]
2
--------------
[[ 0  2  4  7]
 [ 1  1  0 -1]
 [ 3  5  2  1]
 [-1  5  1 -1]
 [ 7  3  5 -2]
 [ 8  7  4 -2]]
4
--------------
Question 6
[2, 1, 3, 4, 2, 2, 0, 1, 1, 3]
[2, 3, 6, 10, 12, 14, 14, 15, 16, 19]
--------------
[1, 2, 1, 4, 4, 1, 0, 2, 4, 4]
[1, 3, 4, 8, 12, 13, 13, 15, 19, 23]
--------------
[3, 2, 2, 1, 2, 3, 1, 4, 0, 2]
[3, 5, 7, 8, 10, 13, 14, 18, 18, 20]
--------------
Question 7
[[4 1 2]
 [3 4 4]]
18
--------------
[[4 4 1 2]
 [3 4 1 2]
 [3 3 3 1]]
26
--------------
[[4 3 1 1 4]
 [4 1 1 4 4]
 [3 3 4 1 1]
 [4 2 1 1 4]]
37
--------------
'''