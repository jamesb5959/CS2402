import btree
import bst
import math
import matplotlib.pyplot as plt

def is_empty(T):
    # T(n) = 1
    return T.data == []

def build_BTree_from_list(L):
    # T(n) = n
    T = btree.BTree()
    for num in L:
        T.insert(num)
    return T

def range_root(t):
    # T(n) = 1 
    return t.data[-1]-t.data[0]

def max_range(t):
    # T(n) = O(n^log_6(6)) = O(n)
    if len(t.child)==0:
        return t.data[-1]-t.data[0]
    max = 0
    for c in t.child:
        max =max_range(c)
        if max < t.data[-1]-t.data[0]:
            max = t.data[-1]-t.data[0]
    return max

def extract_bst(t):
    # T(n) = O(n^log_6(6)) = O(n)
    bt = bst.BST()
    L=[]
    if len(t.child)==0:
        L.append(t.data[0])
    for c in t.child:
        L=extract_bst(c)
        return L
    for i in L:
        bt.insert(i)
    return bt

def prune_leaves(t):
    # T(n) = O(n^log_6(6)) = O(n)
    if len(t.child)==0:
        return t.data
    for c in t.child:
        prune_leaves(c)
    return t

if __name__ == "__main__":
    plt.close('all')

    L1 =  [32,12,58,7,43,3,5,71]
    T0 = btree.BTree()
    T1 = btree.BTree()
    for num in L1:
        T1.insert(num)

    L2 = [31, 32, 6, 3, 23,16, 11, 25, 7, 17,27, 30, 21, 14, 26, 8, 29,
            22, 28, 5, 19, 24, 15, 1, 2, 4, 18, 13, 9, 20, 10, 12]
    T2 = btree.BTree()
    for num in L2:
        T2.insert(num)

    T1.draw()
    T2.draw()

    print('Question 1')
    for T in [T0,T1,T2]:
        print(is_empty(T))
    
    print('Question 2')
    for L in [L1,L2]:
        T = build_BTree_from_list(L)
        T.print_tree()
        T.draw()
        print()

    print('Question 3')
    for T in [T1,T2]:
        print(range_root(T))

    print('Question 4')
    for T in [T1,T2]:
        print(max_range(T))

    print('Question 5')
    for T in [T1,T2]:
        binary_tree = extract_bst(T)
        binary_tree.print_tree()
        binary_tree.draw()
        print()

    print('Question 6')
    for T in [T1,T2]:
        prune_leaves(T)
        T.print_tree()
        T.draw()
        print()

'''
Question 1
True
False
False
Question 2
 [32]
   [3, 5, 7, 12]
   [43, 58, 71]

 [13, 23]
   [3, 7]
     [1, 2]
     [4, 5, 6]
     [8, 9, 10, 11, 12]
   [16, 19]
     [14, 15]
     [17, 18]
     [20, 21, 22]
   [27, 30]
     [24, 25, 26]
     [28, 29]
     [31, 32]

Question 3
0
10
Question 4
28
10
Question 5
    43
 32
    3

       17
    16
       14
 13
       4
    3
       1

Question 6
 [32]

 [13, 23]
   [3, 7]
   [16, 19]
   [27, 30]
'''