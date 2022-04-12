# Arrays exercises
# Rename as lastname_firstname_arrays_ex1.py

import numpy as np
import math

def all_n(n,r,c):
    a = np.zeros((r,c))
    for i in range(r):
        for j in range(c):
            a[i,j]=n
    return a

def sum_row(A,n):
    sum = 0
    for i in range(len(A[0])):
        sum += A[n,i]
    return sum

def sum_column(A,n):
    sum = 0
    for i in range(len(A)):
        sum += A[i,n]
    return sum

def count_vals(a):
    count = np.zeros(10,dtype=np.int16)
    for i in range(len(a)):
        x=0
        for j in range(len(a)):
            if a[i] == a[j]:
                x+=1
        count[a[i]] = x
    return count

def swap_rows(A,i,j):
    B = np.copy(A)
    B[i]=A[j]
    B[j]=A[i]
    return B

def swap_columns(A,i,j):
   B = np.copy(A)
   for x in range(len(A)):
        B[x,i]=A[x,j]
        B[x,j]=A[x,i]
   return B

def replace_greater(A,x,y):
    if len(A.shape)==2:
        for i in range(len(A)):
            for j in range(len(A)):
                if A[i,j]>x:
                    A[i,j]=y
    else:
        for i in range(len(A)):
            if A[i]>x:
                A[i]=y
    return A

if __name__ == "__main__":

    print('Question 1')
    print(all_n(5,3,6))
    print(all_n(10,5,2))

    print('Question 2')
    A = np.arange(20).reshape(4,5)
    print(A)
    for i in range(A.shape[0]):
        print('sum of row',i,'=',sum_row(A,i))

    print('Question 3')
    A = np.arange(20).reshape(4,5)
    print(A)
    for i in range(A.shape[1]):
        print('sum of column',i,'=',sum_column(A,i))

    print('Question 4')
    A1 = np.array([8,3,4,5,1,2,3])
    A2 = np.arange(20)//2
    A3 = np.array([2,4,6,8,8])
    for A in [A1,A2,A3]:
        print('A=',A)
        print('count_vals(A)=',count_vals(A))

    print('Question 5')
    A = np.arange(20).reshape(4,5)
    print(A)
    print(swap_rows(A,0,3))

    print('Question 6')
    A = np.arange(20).reshape(4,5)
    print(A)
    print(swap_columns(A,2,4))

    print('Question 7')
    A = (np.arange(20)*11)%6
    print(A)
    replace_greater(A,3,-1)
    print(A)

    A = (np.arange(20).reshape(4,5))%6
    print(A)
    replace_greater(A,3,-1)
    print(A)

'''
Expected output
Question 1
[[5 5 5 5 5 5]
 [5 5 5 5 5 5]
 [5 5 5 5 5 5]]
[[10 10]
 [10 10]
 [10 10]
 [10 10]
 [10 10]]
Question 2
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]]
sum of row 0 = 10
sum of row 1 = 35
sum of row 2 = 60
sum of row 3 = 85
Question 3
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]]
sum of column 0 = 30
sum of column 1 = 34
sum of column 2 = 38
sum of column 3 = 42
sum of column 4 = 46
Question 4
A= [8 3 4 5 1 2 3]
count_vals(A)= [0 1 1 2 1 1 0 0 1 0]
A= [0 0 1 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8 9 9]
count_vals(A)= [2 2 2 2 2 2 2 2 2 2]
A= [2 4 6 8 8]
count_vals(A)= [0 0 1 0 1 0 1 0 2 0]
Question 5
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]]
[[15 16 17 18 19]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [ 0  1  2  3  4]]
Question 6
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]]
[[ 0  1  4  3  2]
 [ 5  6  9  8  7]
 [10 11 14 13 12]
 [15 16 19 18 17]]
Question 7
[0 5 4 3 2 1 0 5 4 3 2 1 0 5 4 3 2 1 0 5]
[ 0 -1 -1  3  2  1  0 -1 -1  3  2  1  0 -1 -1  3  2  1  0 -1]
[[0 1 2 3 4]
 [5 0 1 2 3]
 [4 5 0 1 2]
 [3 4 5 0 1]]
[[ 0  1  2  3 -1]
 [-1  0  1  2  3]
 [-1 -1  0  1  2]
 [ 3 -1 -1  0  1]]
'''