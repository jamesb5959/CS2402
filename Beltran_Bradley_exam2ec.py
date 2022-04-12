# PLease rename this file as latname_firstname_exam2ec.py
import bst
import btree
import matplotlib.pyplot as plt
import numpy as np

def build_BST_from_list(L):
    # T(n) = O(n log n)
    T = bst.BST()
    for item in L:
        T.insert(item)
    return T

def build_BTree_from_list(L):
    # T(n) = O(n log n)
    T = btree.BTree()
    for item in L:
        T.insert(item)
    return T

def at_depth_d_or_more(T,d):
    # T(n) = O(n)
    if T.is_empty:
        return []
    if d==0:
        return at_depth_d_or_more(T.left,d) + [T.key] + at_depth_d_or_more(T.right,d)
    return at_depth_d_or_more(T.left,d-1) + at_depth_d_or_more(T.right,d-1)
    
def at_depth_d_or_less(T,d):
    # T(n) = 6T(n/6)+c
    count = 0
    L=[]
    if d<0:
        return L
    if d==0 or d>len(T.child):
        return T.data
    for c in T.child:
        L+=at_depth_d_or_less(c,d-1)
        if count != len(T.data):   
            L.append(T.data[count])
        count+=1
    return L
if __name__ == "__main__":

    T0 = build_BST_from_list([])
    T1 = build_BST_from_list([16])
    T2 = build_BST_from_list([4, 12, 6, 5, 10, 2, 7, 16, 14, 0, 3, 20, 11, 9])
    T3 = build_BST_from_list([6, 7, 16, 17, 2, 4, 18, 14, 8, 15, 1, 13,20,5])

    plt.close('all')

    print('Question 1')
    for i, T in enumerate([T0,T1,T2,T3]):
        tree = 'T'+str(i)
       # T.draw(tree)
        for d in range(5):
            print('at_depth_d_or_more({},{}) = '.format(tree,d),end=' ')
            print(at_depth_d_or_more(T,d))
            
    np.random.seed(0)
    T0 = build_BTree_from_list(np.random.permutation(5))
    T1 = build_BTree_from_list(np.random.permutation(10))
    T2 = build_BTree_from_list(np.random.permutation(20))
    T3 = build_BTree_from_list(np.random.permutation(40))

    print('Question 2')
    for i, T in enumerate([T0,T1,T2,T3]):
        tree = 'T'+str(i)
        #T.draw(tree)
        for d in range(-1,3):
            print('at_depth_d_or_less({},{}) = '.format(tree,d),end=' ')
            print(at_depth_d_or_less(T,d))
            
'''
EXPECTED OUTPUT
Question 1
Empty tree, nothing to draw
at_depth_d_or_more(T0,0) =  []
at_depth_d_or_more(T0,1) =  []
at_depth_d_or_more(T0,2) =  []
at_depth_d_or_more(T0,3) =  []
at_depth_d_or_more(T0,4) =  []
at_depth_d_or_more(T1,0) =  [16]
at_depth_d_or_more(T1,1) =  []
at_depth_d_or_more(T1,2) =  []
at_depth_d_or_more(T1,3) =  []
at_depth_d_or_more(T1,4) =  []
at_depth_d_or_more(T2,0) =  [0, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14, 16, 20]
at_depth_d_or_more(T2,1) =  [0, 2, 3, 5, 6, 7, 9, 10, 11, 12, 14, 16, 20]
at_depth_d_or_more(T2,2) =  [0, 3, 5, 6, 7, 9, 10, 11, 14, 16, 20]
at_depth_d_or_more(T2,3) =  [5, 7, 9, 10, 11, 14, 20]
at_depth_d_or_more(T2,4) =  [7, 9, 11]
at_depth_d_or_more(T3,0) =  [1, 2, 4, 5, 6, 7, 8, 13, 14, 15, 16, 17, 18, 20]
at_depth_d_or_more(T3,1) =  [1, 2, 4, 5, 7, 8, 13, 14, 15, 16, 17, 18, 20]
at_depth_d_or_more(T3,2) =  [1, 4, 5, 8, 13, 14, 15, 16, 17, 18, 20]
at_depth_d_or_more(T3,3) =  [5, 8, 13, 14, 15, 17, 18, 20]
at_depth_d_or_more(T3,4) =  [8, 13, 15, 18, 20]
Question 2
at_depth_d_or_less(T0,-1) =  []
at_depth_d_or_less(T0,0) =  [0, 1, 2, 3, 4]
at_depth_d_or_less(T0,1) =  [0, 1, 2, 3, 4]
at_depth_d_or_less(T0,2) =  [0, 1, 2, 3, 4]
at_depth_d_or_less(T1,-1) =  []
at_depth_d_or_less(T1,0) =  [4]
at_depth_d_or_less(T1,1) =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
at_depth_d_or_less(T1,2) =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
at_depth_d_or_less(T2,-1) =  []
at_depth_d_or_less(T2,0) =  [3, 8, 11, 17]
at_depth_d_or_less(T2,1) =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
at_depth_d_or_less(T2,2) =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
at_depth_d_or_less(T3,-1) =  []
at_depth_d_or_less(T3,0) =  [12, 24]
at_depth_d_or_less(T3,1) =  [3, 6, 12, 16, 21, 24, 27, 31, 34]
at_depth_d_or_less(T3,2) =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
'''