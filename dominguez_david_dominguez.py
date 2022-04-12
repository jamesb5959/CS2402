import bst
import btree
import matplotlib.pyplot as plt
import numpy as np
import math

def build_BST_from_list(L):
    # Function is not recursive, no recurrence equation required
    # T(n) = O(n log n) - insertions take log n time, and we perform n of them
    T = bst.BST()
    for item in L:
        T.insert(item)
    return T

def build_BTree_from_list(L): 
   T = btree.BTree()
   for item in L: 
      T.insert(item)
   return T

def is_in_leaf(t,k):
    # T(n) = ?
   node = t.find(k)
   if not node:
      return False

   if node.left.is_empty and node.right.is_empty:
      return True
   return False

 
# 'LRLRLRLR' -> 'RLRLRLR -> LRLRLR -> RLRLR  -> .. -> ''
# T(n) = a T(n/b) + cn^k 
#a: number of recursive calls
#b: how the data is being split over calls
#cn^k: 1 -> n^0 
#k: 0

# a > b^k -> O(n^(logb(a)))
# a == b^k ->  O(n^k logn)
# a < b^k -> O(n^k)

#a: 1
#b: 2
#k: 0

def follow_path(t,S):
   #T(n) = 1 T(n/2) + 1
   # T(n) = log(n)
   if t.is_empty:
      return None

   if S == '':
      return t.key
  
   next_move = S[0]
   S = S[1:]
   if next_move == 'L':
      return follow_path(t.left, S)
   
   if next_move == 'R':
      return follow_path(t.right, S)
   
   return None


# left, root, right: IN-order
# left, right, root: POST-order
# root, left, right: PRE-order

# right, root, left: reversed IN-order

#a: 2
#b: 2
#cn^k: 1 
#k: 0

#2 > 1 
#O(n^1)
def reversed_in_order_list(t):
   # T(n) = 2 T(n/2) + 1
   #T(n) = O(n)
   if t.is_empty:
      return []

   return reversed_in_order_list(t.right) + [t.key] + reversed_in_order_list(t.left)

#in-order traversal
def internal_nodes(t):
   # T(n) = O(n)
   if t.is_empty:
      return []
   
   if t.right.is_empty and t.left.is_empty:
      return []
   

   return internal_nodes(t.left) + [t.key] + internal_nodes(t.right)


def copy_bst_up_to_depth_d(t,d):
   # T(n) = O(n)
   if t.is_empty:
      return t

   if d == 0:
      return bst.BST(key=t.key)
   
   left = copy_bst_up_to_depth_d(t.left, d-1)
   right = copy_bst_up_to_depth_d(t.right, d-1)
   return bst.BST(t.key, left, right)



#BTree is also a BST (it is sorted in order)
#The maximum element in each node is in data[-1]
#In each level the node with the maximum element is on the right
#to get each max element we want to keep traversing right

def largest_at_every_depth(t):
   # T(n) = 1 T(n/6) + 1
   # T(n) = log6(n)
   if len(t.child) == 0:
      return [t.data[-1]]

   return [t.data[-1]] + largest_at_every_depth(t.child[-1])

#min amount of keys -> min_amount_of_children - 1
#min_amoun_of_children -> max_items + 1 /2 
#max_amount_of_children -> max+items+1
#max_amount_of_items -> 


def delete_if_legal(t,k):
   # T(n) = 1 T(n/6) + 1
   #a: 1
   #b: 6
   #k: 0

   # 1 = 1 
   #O(logn)

   if k in t.data:
      #it is in a leaf-node and has minimum number of keys
      if len(t.child) == 0 and len(t.data) > ((t.max_items+1)//2)-1:
         t.data.remove(k)
         return True
         
      return False
   #still possible to traverse
   elif len(t.child) != 0:
      possible_child = t.find_subtree(k)
      return delete_if_legal(t.child[possible_child], k)
      
   return False


def even_items(t):
    # T(n) = ?
   if len(t.child) == 0:
      return filter(lambda x: x%2==0, t.data)
   
   retL = []
   for i in range(len(t.data)):

      retL+=even_items(t.child[i])

      if t.data[i]%2 ==0:
         retL.append(t.data[i])
         
   retL+=even_items(t.child[-1])

   return retL

def shrink_leaves(t):
   if len(t.child) == 0:
      t.data = t.data[:2]
      return
   
   for c in t.child:
      shrink_leaves(c)


if __name__ == "__main__":
    A = [9, 6, 7, 16, 17, 2, 4, 18, 14, 8, 15, 1, 13,20]
    B = [8, 4, 12, 6, 5, 10, 2, 7, 16, 14, 0, 3, 20, 11, 9]
    C = [1,2,3]
    D = [5,9,1]
    E = [11]
    F = []

    TA = build_BST_from_list(A)
    TB = build_BST_from_list(B)
    TC = build_BST_from_list(C)
    TD = build_BST_from_list(D)
    TE = build_BST_from_list(E)
    TF = build_BST_from_list(F)

    plt.close('all')
    plt.rcParams.update({'figure.max_open_warning': 0})

    print('Question 1')

    k = 11
    print(k,is_in_leaf(TE,k))
    print(k,is_in_leaf(TF,k))

    TA.draw('Tree for questions 1 and 2')
    for k in range(21):
        print(k,is_in_leaf(TA,k))

    print('Question 2')
    for p in ['','L','R','LL','LR','RRRR','LLLL']:
        print(p,follow_path(TA,p))

    print('Question 3')
    for T in [TA,TB,TC,TD,TE,TF]:
        T.draw('Tree for questions 3 and 4')
        print(reversed_in_order_list(T))

    print('Question 4')
    for T in [TA,TB,TC,TD,TE,TF]:
        print(internal_nodes(T))

    print('Question 5')
    T5 = build_BST_from_list([ 9, 12, 16,  1, 17, 11, 19,  5,  6,  7,  0,  3,  2, 14, 18,  4, 10, 13, 15, 8])
    T5.draw('Tree for question 5')
    for d in range(7):
        T = copy_bst_up_to_depth_d(T5,d)
        T.draw('Question 5, d='+str(d))  # Uncomment to visualize
        print('d =',d)
        T.print_tree()

    print('Question 6')
    T1 = build_BTree_from_list(np.arange(0,40,2))
    T2 = build_BTree_from_list(np.arange(1,60,2))
    T1.draw('T1 for question 6')
    T2.draw('T2 for question 6')
    for T in [T1,T2]:
        print(largest_at_every_depth(T))

    print('Question 7')
    for i in range(1):
        np.random.seed(i+2)
        n = np.random.randint(20,30)
        L = np.random.permutation(n+10)[:n]*2
        T = build_BTree_from_list(L)
        T.draw('Tree for question 7')
        for k in L[-3:]:
            if delete_if_legal(T,k):
                T.draw(str(k)+' was deleted')
            else:
                print(k,'could not be deleted')

    print('Question 8')
    np.random.seed(8)
    T1 = build_BTree_from_list(np.random.permutation(30)[:20])
    T2 = build_BTree_from_list(np.random.permutation(40)[:30])
    T1.draw('T1 for question 8')
    T2.draw('T2 for question 8')
    for T in [T1,T2]:
        print(even_items(T))

    print('Question 9')
    np.random.seed(9)
    T1 = build_BTree_from_list(np.random.permutation(30)[:20])
    T2 = build_BTree_from_list(np.random.permutation(40)[:30])

    for T in [T1,T2]:
        T.draw('Tree for question 9')
        shrink_leaves(T)
        T.print_tree()
        T.draw('Question 9 result')
        print()

'''
Question 1
11 True
11 False
0 False
1 True
2 False
3 False
4 True
5 False
6 False
7 False
8 True
9 False
10 False
11 False
12 False
13 True
14 False
15 True
16 False
17 False
18 False
19 False
20 True
Question 2
 9
L 6
R 16
LL 2
LR 7
RRRR 20
LLLL None
Question 3
[20, 18, 17, 16, 15, 14, 13, 9, 8, 7, 6, 4, 2, 1]
[20, 16, 14, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 0]
[3, 2, 1]
[9, 5, 1]
[11]
Empty tree, nothing to draw
[]
Question 4
[2, 6, 7, 9, 14, 16, 17, 18]
[2, 4, 6, 8, 10, 12, 16]
[1, 2]
[5]
[]
[]
Question 5
d = 0
 9
d = 1
    12
 9
    1
d = 2
       16
    12
       11
 9
       5
    1
       0
d = 3
          17
       16
          14
    12
       11
          10
 9
          6
       5
          3
    1
       0
d = 4
             19
          17
       16
             15
          14
             13
    12
       11
          10
 9
             7
          6
       5
             4
          3
             2
    1
       0
d = 5
             19
                18
          17
       16
             15
          14
             13
    12
       11
          10
 9
                8
             7
          6
       5
             4
          3
             2
    1
       0
d = 6
             19
                18
          17
       16
             15
          14
             13
    12
       11
          10
 9
                8
             7
          6
       5
             4
          3
             2
    1
       0
Question 6
[16, 28, 38]
[35, 53, 59]
Question 7
40 could not be deleted
Question 8
[0, 2, 4, 6, 10, 12, 14, 18, 22, 26, 28]
[0, 4, 6, 8, 10, 12, 14, 16, 18, 24, 26, 30, 32, 34, 36]
Question 9
 [4, 7, 12, 18]
   [0, 2]
   [5, 6]
   [9, 10]
   [13, 14]
   [19, 23]

 [19]
   [7, 14]
     [0, 1]
     [8, 10]
     [15, 17]
   [27, 31, 35]
     [20, 23]
     [28, 30]
     [32, 34]
     [36, 38]
'''