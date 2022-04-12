import numpy as np

class stack:
    def __init__(self):
        # T(n) = O(1)
        self.data = []

    def push(self,item):
        # T(n) = O(?)
        #O(1) because its just inserting it.
        return self.data.append(item)

    def pop(self):
        # T(n) = O(?)
        #O(1) because it reads it and deletes it.
        if len(self.data)==0:
            return None
        return self.data.pop(-1)

    def print_stack(self):
        #O(n) because it prints all elements in a list
        return print(self.data)

    def is_empty(self):
        # T(n) = O(?)
        #o(1) because it it has one element it is false.
        if len(self.data)!=0:
            return False
        return True

def multiples(k,m):
    # T(n) = O(?)
    #O(n) because it makes a list of multiples till me    
    return [i for i in range(m) if i%k==0]

def swap(L,i,j):
    # T(n) = O(?)
    #O(1) because it just swaps
    temp = L[i]
    L[i]=L[j]
    L[j]=temp
    return L

def move_to_end(L,i):
    # T(n) = O(?)
    #o(1) to swap the end and i
    temp = L[i]
    L[i]=L[-1]
    L[-1]=temp
    return L

def reverse_last_k(L,k):
    # T(n) = O(?)
    #O(1) to rewrite and reverse the last k elements
    L1=[]
    L1=L[:len(L)-k]+L[-k::-1]
    return L1

def row_plus_col(A1,A2):
    # T(r,c) = O(?)
    #O(n) because it has a for loop
    A3=np.zeros((len(A2), len(A1)))
    for i in range(len(A1)):
        for j in range(len(A2)):
            A3[j,i]=A1[i]+A2[j]
    return A3

def first_and_last_row(A):
    # T(r,c) = O(?)
    #O(1) because it just gets the first and last row.
    A1 = np.zeros((2, len(A[0])))
    A1[0]=A[0]
    A1[-1]=A[-1]
    return A1

def reshape_to_cols(A,c):
    # T(n) = O(?)
    #O(n) because it has a for loop and it needs to reshap and rewrite a array.
    x=len(A)
    copy = np.copy(A)
    for i in range(len(A)):
        if x%c!=0:
            x=x-1
            copy[:len(copy)-1]
        if x%c==0:
            break
    A1=np.zeros(x,c)
    z=0
    for i in range(len(A)):
        for j in range(c):
            A1[i,j]=copy[j+z]
        z=z+c
    return A1

if __name__ == "__main__":

    print('Question 1')
    s = stack()
    print(s.pop())
    for i in [2,5,6,7,9]:
        s.push(i)
        s.print_stack()
    L = []
    while not s.is_empty():
        p = s.pop()
        s.print_stack()
        L.append(p)
    print(L)

    print('Question 2')
    for k in [1,2,3,5]:
        print('k =',k)
        print(multiples(k,20))

    print('Question 3')
    L1 = [6, 4, 8, 9]
    L2 = [0, 12, 9, 6, 3, 4]
    L3 = list(np.arange(6)*10)

    print(L1)
    swap(L1,0,1)
    print(L1)

    print(L2)
    swap(L2,4,2)
    print(L2)

    print(L3)
    swap(L3,3,1)
    print(L3)

    print('Question 4')
    L1 = [6, 4, 8, 9]
    L2 = [0, 12, 9, 6, 3, 4]
    L3 = list(np.arange(6)*10)

    print(L1)
    move_to_end(L1,1)
    print(L1)

    print(L2)
    move_to_end(L2,2)
    print(L2)

    print(L3)
    move_to_end(L3,4)
    print(L3)

    print('Question 5')
    L1 = [6, 4, 8, 9, 3, 7, 9]
    L2 = [0, 12, 9, 6, 3, 4]
    L3 = list(np.arange(6)*10)

    print(L1)
    reverse_last_k(L1,3)
    print(L1)

    print(L2)
    reverse_last_k(L2,5)
    print(L2)

    print(L3)
    reverse_last_k(L3,2)
    print(L3)

    print('Question 6')
    A1 = np.array([6, 4, 8, 9, 3, 7, 9])
    A2 = np.arange(5)
    A3 = np.arange(-1,2)

    print(A1)
    print(A2)
    print(row_plus_col(A1,A2))

    print(A1)
    print(A3)
    print(row_plus_col(A1,A3))

    print(A2)
    print(A3)
    print(row_plus_col(A2,A3))

    print('Question 7')
    np.random.seed(1)
    A1 = np.random.randint(0,10,size=(5,6))
    A2 = np.random.randint(0,10,size=(1,8))
    A3 = np.random.randint(0,10,size=(4,5))

    for A in [A1,A2,A3]:
        print(A)
        print(first_and_last_row(A))

    print('Question 8')
    np.random.seed(8)
    A1 = np.random.randint(0,10,size=8)
    A2 = np.random.randint(0,10,size=12)
    A3 = np.random.randint(0,10,size=17)

    for A in [A1,A2,A3]:
        print(A)
        print(reshape_to_cols(A,3))

    for A in [A1,A2,A3]:
        print(A)
        print(reshape_to_cols(A,5))

'''
Question 1
None
[2]
[2, 5]
[2, 5, 6]
[2, 5, 6, 7]
[2, 5, 6, 7, 9]
[2, 5, 6, 7]
[2, 5, 6]
[2, 5]
[2]
[]
[9, 7, 6, 5, 2]
Question 2
k = 1
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
k = 2
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
k = 3
[0, 3, 6, 9, 12, 15, 18]
k = 5
[0, 5, 10, 15]
Question 3
[6, 4, 8, 9]
[4, 6, 8, 9]
[0, 12, 9, 6, 3, 4]
[0, 12, 3, 6, 9, 4]
[0, 10, 20, 30, 40, 50]
[0, 30, 20, 10, 40, 50]
Question 4
[6, 4, 8, 9]
[6, 8, 9, 4]
[0, 12, 9, 6, 3, 4]
[0, 12, 6, 3, 4, 9]
[0, 10, 20, 30, 40, 50]
[0, 10, 20, 30, 50, 40]
Question 5
[6, 4, 8, 9, 3, 7, 9]
[6, 4, 8, 9, 9, 7, 3]
[0, 12, 9, 6, 3, 4]
[0, 4, 3, 6, 9, 12]
[0, 10, 20, 30, 40, 50]
[0, 10, 20, 30, 50, 40]
Question 6
[6 4 8 9 3 7 9]
[0 1 2 3 4]
[[ 6  4  8  9  3  7  9]
 [ 7  5  9 10  4  8 10]
 [ 8  6 10 11  5  9 11]
 [ 9  7 11 12  6 10 12]
 [10  8 12 13  7 11 13]]
[6 4 8 9 3 7 9]
[-1  0  1]
[[ 5  3  7  8  2  6  8]
 [ 6  4  8  9  3  7  9]
 [ 7  5  9 10  4  8 10]]
[0 1 2 3 4]
[-1  0  1]
[[-1  0  1  2  3]
 [ 0  1  2  3  4]
 [ 1  2  3  4  5]]
Question 7
[[5 8 9 5 0 0]
 [1 7 6 9 2 4]
 [5 2 4 2 4 7]
 [7 9 1 7 0 6]
 [9 9 7 6 9 1]]
[[5 8 9 5 0 0]
 [9 9 7 6 9 1]]
[[0 1 8 8 3 9 8 7]]
[[0 1 8 8 3 9 8 7]
 [0 1 8 8 3 9 8 7]]
[[3 6 5 1 9]
 [3 4 8 1 4]
 [0 3 9 2 0]
 [4 9 2 7 7]]
[[3 6 5 1 9]
 [4 9 2 7 7]]
Question 8
[3 4 1 9 5 8 3 8]
[[3 4 1]
 [9 5 8]]
[0 5 1 3 9 2 2 6 8 9 3 4]
[[0 5 1]
 [3 9 2]
 [2 6 8]
 [9 3 4]]
[5 5 7 9 2 6 9 5 1 6 4 5 8 0 7 2 6]
[[5 5 7]
 [9 2 6]
 [9 5 1]
 [6 4 5]
 [8 0 7]]
[3 4 1 9 5 8 3 8]
[[3 4 1 9 5]]
[0 5 1 3 9 2 2 6 8 9 3 4]
[[0 5 1 3 9]
 [2 2 6 8 9]]
[5 5 7 9 2 6 9 5 1 6 4 5 8 0 7 2 6]
[[5 5 7 9 2]
 [6 9 5 1 6]
 [4 5 8 0 7]]
'''