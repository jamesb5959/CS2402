# PLease rename this file as latname_firstname_exam2.py
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

def count_nodes(t):
    # T(n) = 2T(n/2) + 1
    # T(n) = O(n)
    if t.is_empty:
        return 0
    return 1 + count_nodes(t.left) + count_nodes(t.right)

def in_roots_children(T,k):
    # T(n) = O(1)
    if T.is_empty:
        return False
    c =[t.key for t in [T.left,T.right] if not t.is_empty]
    return k in c

def num_descendants(T,k):
    # T(n) = O(n) - time required by count nodes, since find takes O(log n) time
    x = T.find(k)
    if x==None:
        return -1
    return count_nodes(x.left) + count_nodes(x.right)

def at_depth_d_or_less(T,d):
    # T(n) = 2T(n/2) + 1
    # T(n) = O(n)
    if T.is_empty or d<0:
        return []
    return at_depth_d_or_less(T.left,d-1) + [T.key] + at_depth_d_or_less(T.right,d-1)

def is_root_full(T):
    # T(n) = O(1)
    return len(T.data)==T.max_items

def smallest_at_every_depth(T):
    # T(n) = O(log n)
    L = [T.data[0]]
    if len(T.child)>0:
        L = smallest_at_every_depth(T.child[0]) + L
    return L

def largest_in_every_leaf(T):
    # T(n) = O(n)
    if len(T.child)==0:
        return [T.data[-1]]
    L = []
    for c in T.child:
        L = L + largest_in_every_leaf(c)
    return L

def ks_children(T,k):
    # T(n) = O(log n)
    if k in T.data:
        return len(T.child)
    if len(T.child)==0:
        return -1
    s = T.find_subtree(k)
    return ks_children(T.child[s],k)

if __name__ == "__main__":

    T0 = build_BST_from_list([])
    T1 = build_BST_from_list([16])
    T2 = build_BST_from_list([4, 12, 6, 5, 10, 2, 7, 16, 14, 0, 3, 20, 11, 9])
    T3 = build_BST_from_list([6, 7, 16, 17, 2, 4, 18, 14, 8, 15, 1, 13,20,5])

    plt.close('all')

    for i, T in enumerate([T0,T1,T2,T3]):
        T.draw('T'+str(i))

    print('Question 1')
    for i, T in enumerate([T0,T1,T2,T3]):
        tree = 'T'+str(i)
        for k in [2,7,12]:
            print('in_roots_children({},{}) = {}'.format(tree,k,in_roots_children(T,k)))

    print('Question 2')
    for i, T in enumerate([T0,T1,T2,T3]):
        tree = 'T'+str(i)
        for k in [7,12,14,16]:
            print('num_descendants({},{}) = {}'.format(tree,k,num_descendants(T,k)))

    print('Question 3')
    for i, T in enumerate([T1,T2,T3]):
        tree = 'T'+str(i+1)
        for d in range(5):
            print('at_depth_d_or_less({},{}) = '.format(tree,d),end=' ')
            print(at_depth_d_or_less(T,d))

    np.random.seed(0)
    T0 = build_BTree_from_list(np.random.permutation(5))
    T1 = build_BTree_from_list(np.random.permutation(10))
    T2 = build_BTree_from_list(np.random.permutation(20))
    T3 = build_BTree_from_list(np.random.permutation(40))

    for i, T in enumerate([T0,T1,T2,T3]):
        T.draw('T'+str(i))

    print('Question 4')
    for i, T in enumerate([T0,T1,T2,T3]):
        tree = 'T'+str(i)
        print('is_root_full({}) = {}'.format(tree,is_root_full(T)))

    print('Question 5')
    for i, T in enumerate([T0,T1,T2,T3]):
        tree = 'T'+str(i)
        print('smallest_at_every_depth({}) = {}'.format(tree,smallest_at_every_depth(T)))

    print('Question 6')
    for i, T in enumerate([T0,T1,T2,T3]):
        tree = 'T'+str(i)
        print('largest_in_every_leaf({}) = {}'.format(tree,largest_in_every_leaf(T)))

    print('Question 7')
    for i, T in enumerate([T0,T1,T2,T3]):
        tree = 'T'+str(i)
        for k in [4,8,12]:
            print('ks_children({},{}) = {}'.format(tree,k,ks_children(T,k)))


'''
Empty tree, nothing to draw
Question 1
in_roots_children(T0,2) = False
in_roots_children(T0,7) = False
in_roots_children(T0,12) = False
in_roots_children(T1,2) = False
in_roots_children(T1,7) = False
in_roots_children(T1,12) = False
in_roots_children(T2,2) = True
in_roots_children(T2,7) = False
in_roots_children(T2,12) = True
in_roots_children(T3,2) = True
in_roots_children(T3,7) = True
in_roots_children(T3,12) = False
Question 2
num_descendants(T0,7) = -1
num_descendants(T0,12) = -1
num_descendants(T0,14) = -1
num_descendants(T0,16) = -1
num_descendants(T1,7) = -1
num_descendants(T1,12) = -1
num_descendants(T1,14) = -1
num_descendants(T1,16) = 0
num_descendants(T2,7) = 1
num_descendants(T2,12) = 9
num_descendants(T2,14) = 0
num_descendants(T2,16) = 2
num_descendants(T3,7) = 8
num_descendants(T3,12) = -1
num_descendants(T3,14) = 3
num_descendants(T3,16) = 7
Question 3
at_depth_d_or_less(T0,0) =  []
at_depth_d_or_less(T1,0) =  [16]
at_depth_d_or_less(T1,1) =  [16]
at_depth_d_or_less(T1,2) =  [16]
at_depth_d_or_less(T2,0) =  [4]
at_depth_d_or_less(T2,1) =  [2, 4, 12]
at_depth_d_or_less(T2,2) =  [0, 2, 3, 4, 6, 12, 16]
at_depth_d_or_less(T2,3) =  [0, 2, 3, 4, 5, 6, 10, 12, 14, 16, 20]
at_depth_d_or_less(T2,4) =  [0, 2, 3, 4, 5, 6, 7, 10, 11, 12, 14, 16, 20]
at_depth_d_or_less(T3,0) =  [6]
at_depth_d_or_less(T3,1) =  [2, 6, 7]
at_depth_d_or_less(T3,2) =  [1, 2, 4, 6, 7, 16]
at_depth_d_or_less(T3,3) =  [1, 2, 4, 5, 6, 7, 14, 16, 17]
at_depth_d_or_less(T3,4) =  [1, 2, 4, 5, 6, 7, 8, 14, 15, 16, 17, 18]
at_depth_d_or_less(T3,5) =  [1, 2, 4, 5, 6, 7, 8, 13, 14, 15, 16, 17, 18, 20]
at_depth_d_or_less(T3,6) =  [1, 2, 4, 5, 6, 7, 8, 13, 14, 15, 16, 17, 18, 20]
Question 4
is_root_full(T0) = True
is_root_full(T1) = False
is_root_full(T2) = False
is_root_full(T3) = False
Question 5
smallest_at_every_depth(T0) = [0]
smallest_at_every_depth(T1) = [0, 4]
smallest_at_every_depth(T2) = [0, 3]
smallest_at_every_depth(T3) = [0, 3, 12]
Question 6
largest_in_every_leaf(T0) = [4]
largest_in_every_leaf(T1) = [3, 9]
largest_in_every_leaf(T2) = [2, 7, 10, 16, 19]
largest_in_every_leaf(T3) = [2, 5, 11, 15, 20, 23, 26, 30, 33, 39]
Question 7
ks_children(T0,4) = 0
ks_children(T0,8) = -1
ks_children(T0,12) = -1
ks_children(T1,4) = 2
ks_children(T1,8) = 0
ks_children(T1,12) = -1
ks_children(T2,4) = 0
ks_children(T2,8) = 5
ks_children(T2,12) = 0
ks_children(T3,4) = 0
ks_children(T3,8) = 0
ks_children(T3,12) = 3
'''
