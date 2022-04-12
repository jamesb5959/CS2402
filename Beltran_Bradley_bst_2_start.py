import bst
import matplotlib.pyplot as plt
import numpy as np

def build_bst(L):
  T = bst.BST()
  for a in L:
    T.insert(a)
  return T

def smaller_than(t,k):
   L=[]
   if t.is_empty:
      return []
   if t.key<k:
      L=[t.key]
      return smaller_than(t.left, k)+L+smaller_than(t.right, k)
   else:
      return smaller_than(t.right, k)+smaller_than(t.left, k)
   return L

def path_string(t,k):
   if k==t.key:
      return ""
   if k>t.key and t.right.is_empty:
        return 'R'
   if k<t.key and t.left.is_empty:
        return 'L'
   if k>=t.key:
        return 'R'+path_string(t.right,k)
   if k<t.key:
        return 'L'+path_string(t.left,k)
    
def remove_descendants(t,k):
   x = t.find(k)
   while not x.right.is_empty: 
      t.delete(x.right.key)
   while not x.left.is_empty:
      t.delete(x.left.key)
   return t
   
def is_left_child(t,k):
   if t.right.is_empty or t.left.is_empty:
      return False
   if t.right.key == k:
      return False
   if t.left.key == k:
      return True
   if k>t.key:
      return is_left_child(t.right,k)
   if k<t.key:
      return is_left_child(t.left,k)
   return False

def is_full(t):
   if t.is_empty:
        return True
   if t.left.is_empty and t.right.is_empty:
        return True
   if t.left.is_empty and not t.right.is_empty:
        return False
   if t.right.is_empty and not t.left.is_empty:
        return False
   return is_full(t.left) and is_full(t.right)
    
if __name__ == "__main__":

    L =[9, 11, 6, 7, 16, 17, 2, 4, 19, 14, 8, 15, 1, 20, 13,18,21]
    
    T = build_bst(L)

    plt.close('all')
    T.draw()

    print('Question 1')
    for k in [0,5,10,15,20,25]:
        print(k, smaller_than(T,k))

    print('Question 2')
    for k in [0,5,10,15,20]:
        print(k, path_string(T,k))

    print('Question 3')
    T.print_tree()
    remove_descendants(T,19)
    T.print_tree()
    print('----------------------')
    T.draw()
    remove_descendants(T,14)
    T.print_tree()
    print('----------------------')
    T.draw()
    remove_descendants(T,6)
    T.print_tree()
    print('----------------------')
    T.draw()
    remove_descendants(T,9)
    T.print_tree()
    print('----------------------')
    T.draw()

    print('Question 4')
    np.random.seed(1)
    T = build_bst(L)

    for k in [0,5,8,10,15,20]:
        print(k,is_left_child(T,k))

    print('Question 5')

    print(is_full(bst.BST()))
    
    T = build_bst([5,1,8])
    T.draw()
    print(is_full(T))
    
    T = build_bst([5,1,8,9])
    T.draw()
    print(is_full(T))
    
    T = build_bst([5,1,8,9,6])
    T.draw()
    print(is_full(T))

    T = build_bst([9, 11, 6, 7, 16, 17, 2, 4, 19, 14, 8, 15, 1, 20, 13,18,21])
    T.draw()
    print(is_full(T))
    
    T = build_bst([9, 11, 6, 7, 16, 18, 2, 4, 19, 14, 15, 1, 13,17,10])
    T.draw()
    print(is_full(T))

'''
Expected results:
Question 1
0 []
5 [1, 2, 4]
10 [1, 2, 4, 6, 7, 8, 9]
15 [1, 2, 4, 6, 7, 8, 9, 11, 13, 14]
20 [1, 2, 4, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 18, 19]
25 [1, 2, 4, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21]
Question 2
0 LLLL
5 LLRR
10 RL
15 RRLR
20 RRRRR
Question 3
                   21
                20
             19
                18
          17
       16
             15
          14
             13
    11
 9
          8
       7
    6
          4
       2
          1
             19
          17
       16
             15
          14
             13
    11
 9
          8
       7
    6
          4
       2
          1
----------------------
             19
          17
       16
          14
    11
 9
          8
       7
    6
          4
       2
          1
----------------------
             19
          17
       16
          14
    11
 9
    6
----------------------
 9
----------------------
Question 4
0 False
5 False
8 False
10 False
15 False
20 False
Question 5
True
True
False
True
False
True
'''