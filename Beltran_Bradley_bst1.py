# Starter code for binary search trees, exercise 1
# rename as lastname_firstname_bst1.py

import bst
import numpy as np
import matplotlib.pyplot as plt

def num_children(t,k):
    x  =  t.find(k)
    count = 0
    if x is None:
        return -1
    if not x.right.is_empty:
        count =count+1
    if not x.left.is_empty:
        count =count+1
    return count

def path_to_largest(t):
    path = [t.key]
    if t.right.is_empty:
        return path
    return path+path_to_largest(t.right)

def path_to_k(t,k):
    L = [t.key]
    if t.right.is_empty or t.left.is_empty:
        return L
    if k>=t.key:
        return L+path_to_k(t.right,k)
    if k<t.key:
        return L+path_to_k(t.left,k)

def leaves(t):
    L = []
    if t.is_empty:
        return L
    if t.left:
        L.extend(leaves(t.left))
    if t.right:
        L.extend(leaves(t.right))
    if not L:
        L = [t.key]
    return L

def at_depth_d(t,d):
    L=[]
    if t.is_empty:
        return L
    if d==0:
        L=[t.key]
        return L
    return at_depth_d(t.left,d-1) + at_depth_d(t.right,d-1)
    

if __name__ == "__main__":

    A =[8, 15, 5, 13, 11, 6, 7, 2, 4, 18, 1,19,20 ]

    T = bst.BST()

    for a in A:
        T.insert(a)

    plt.close('all')
    T.draw()

    print('Question 1')
    for k in [8,2,13,6,11,4,0,19]:
        print(k, num_children(T,k))

    print('Question 2')
    print(path_to_largest(T))

    print('Question 3')
    for k in A:
        print(k, path_to_k(T,k))

    print('Question 4')
    print(leaves(T))

    print('Question 5')
    for i in range(6):
        print(at_depth_d(T,i))

'''
Expected output:
Question 1
8 2
2 2
13 1
6 1
11 0
4 0
0 -1
19 1
Question 2
[8, 15, 18, 19, 20]
Question 3
8 [8]
15 [8, 15]
5 [8, 5]
13 [8, 15, 13]
11 [8, 15, 13, 11]
6 [8, 5, 6]
7 [8, 5, 6, 7]
2 [8, 5, 2]
4 [8, 5, 2, 4]
18 [8, 15, 18]
1 [8, 5, 2, 1]
19 [8, 15, 18, 19]
20 [8, 15, 18, 19, 20]
Question 4
[1, 4, 7, 11, 20]
Question 5
[8]
[5, 15]
[2, 6, 13, 18]
[1, 4, 7, 11, 19]
[20]
[]
'''