import numpy as np
import math

def all_n(n,r,c):
    return np.zeros((r,c),dtype=np.int32)+n

def sum_row(A,n):
    return np.sum(A[n])

def sum_column(A,n):
    return np.sum(A[:,n])

def count_vals(A):
    count = np.zeros(10,dtype=np.int16)
    for i in A:
        count[i] +=1
    return count

def swap_rows(A,i,j):
    # O(n)
    B = np.copy(A)
    B[i] = A[j]
    B[j] = A[i]
    return B

def swap_columns(A,i,j):
   B = np.copy(A)
   B[:,i] = A[:,j]
   B[:,j] = A[:,i]
   return B

def replace_greater(A,x,y):
    A[A>x] = y

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