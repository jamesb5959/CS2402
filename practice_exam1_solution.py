import numpy as np

class stack:
    def __init__(self):
        # T(n) = O(1)
        self.data = []

    def push(self,item):
        # T(n) = O(1)
        self.data.append(item)

    def pop(self):
        # T(n) = O(1)
        if not self.is_empty():
            return self.data.pop()

    def print_stack(self):
        # T(n) = O(n)
        print(self.data)

    def is_empty(self):
        # T(n) = O(1)
        return len(self.data)==0

def multiples(k,n):
    # T(n) = O(n)
    return [i for i in range(0,n,k)]

def swap(L,i,j):
    # T(n) = O(1)
    L[i],L[j] = L[j],L[i]

def move_to_end(L,i):
    # T(n) = O(1)
    p = L.pop(i)
    L.append(p)

def reverse_last_k(L,k):
    # T(n) = O(n)
    L[-k:] = L[-1:-k-1:-1]

def row_plus_col(A1,A2):
    # T(r,c) = O(r*c)
    return A1.reshape(1,-1) + A2.reshape(-1,1)

def first_and_last_row(A):
    # T(r,c) = O(c)
    return A[[0,-1]]

def reshape_to_cols(A,c):
    # T(n) = O(n)
    r = len(A)//c
    return A[:r*c].reshape(-1,c)

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