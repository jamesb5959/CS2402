import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

import bst
from utils import draw_list_bst

# ******************** PROVIDED FUNCTIONS ********************
def insert(T, item):
    # Inserts an item to a BST
    # Running time is O(log n) for a balanced tree
    if T == None:  # T is empty
        # T = [left, key, right]
        T = [None, item, None]
    else:
        # Compare our item against the key of the current subtree (T[1]) to decide
        # whether to insert it in the left subtree (T[0]) or the right one (T[2])
        key = T[1]
        if item < key:
            T[0] = insert(T[0], item) # Insert the key in the left subtree
        else:
            T[2] = insert(T[2], item) # Insert the key in right subtree
    return T

def in_order(T):
    # Prints keys in the tree in ascending order
    # Running time is O(n) for a balanced or unbalanced tree
    if T != None:
        # T is not empty, so let's use 3 different variables to make our lives easier
        # Remember, you can't do this unless you check that T is not None
        left_subtree = T[0]
        key = T[1]
        right_subtree = T[2]

        in_order(left_subtree)
        print(key, end=' ')
        in_order(right_subtree)
    
def leaves(T):
    # 1st Base Case: If the subtree T is empty
    if T == None:
        return []

    # T is not empty, so let's use 3 different variables to make our lives easier
    # Remember, you can't do this unless you check that T is not None
    left_subtree = T[0]
    key = T[1]
    right_subtree = T[2]

    # 2nd Base Case: Check if we are in a leaf
    if left_subtree == None and right_subtree == None:
        return [key]

    return leaves(left_subtree) + leaves(right_subtree)

# ******************** LAB PROBLEMS (WRITE YOUR CODE HERE) ********************
def size(T):
    count = 0
    if not T is None:
        count = size(T[0]) 
        count+=1
        count = count + size(T[2])
    return count

def minimum(T):
    if T is None:
        return None
    if T[0] is None:
        return T[1]
    return minimum(T[0])

def maximum(T):
    if T is None:
        return None
    if T[2] is None:
        return T[1]
    return maximum(T[2])

def height(T):
    if T is None:
        return -1
    return 1 + max(height(T[0]),height(T[2]))

def in_tree(T, item):
    if T is None:
        return False
    if T[1] == item:
        return True
    if T[1]>item:
        return in_tree(T[0], item)
    return in_tree(T[2], item)

def print_by_level(T):
    Q = [T]
    while len(Q)>0:
        p = Q.pop(0)
        if not p is None:
            print(p[1],end=' ')
            Q.append(p[0])
            Q.append(p[2])
    print('')

def items_at_depth_d(T, d):
    L=[]
    if d==0 and not T is None:
      L.append(T[1])
    if d!=0 and not T is None:
        L = items_at_depth_d(T[0],d-1)
        L = L + items_at_depth_d(T[2],d-1) 
    return L

def depth_of_k(T, k):
    count = 0
    while T is not None:
        if T[1]==k:
            return count
        if k>T[1]:
            count+=1
            T=T[2]
        if k<T[1]:
            count+=1
            T=T[0]
    return -1
    if T is None:
        return d
    if T[1]==k:
        return d+1
    if k>T[1]:
        d+=1
        d=d+depth_of_k(T[2],k)
    if k<T[1]:
        d+=1
        d=d+depth_of_k(T[0],k)
    return d

def tree_to_list_stack(T):
    L=[]
    Q = [T]
    while len(Q)>0:
        p = Q.pop(0)
        if not p is None:
            L.append(p[1])
            Q.append(p[0])
            Q.append(p[2])
    L.sort()
    return L
    L=[]
    if not T is None:
        L = tree_to_list_stack(T[0]) 
        L.append(T[1])
        L = L + tree_to_list_stack(T[2])
    return L

def is_full(T):
    if T is None:
        return True
    if T[0] is None and T[2] is None:
        return True
    if T[0] is None and not T[2] is None:
        return False
    if T[2] is None and not T[0] is None:
        return False
    return is_full(T[0]) and is_full(T[2])

def is_perfect(T):
    if T is None:
        return True
    Temp = T
    depth = 0
    count = 0
    while Temp is not None:
        depth += 1
        Temp = Temp[0]
    if T[0] is None and T[2] is None:
        return depth == count+1
    if T[0] is None and T[2] is None:
        return False
    count+=1
    return count+is_perfect(T[0]) and is_perfect(T[2])

def delete(T, k):
    if T is None:
        return T
    if k < T[1]:
        T[0] = delete(T[0], k)
    if k > T[1]:
        T[2] = delete(T[2], k)
    else:
        if T[0] is None:
            temp = T[2]
            root = None
            return temp
        if T[2] is None:
            temp = T[0]
            root = None
            return temp
        new = minimum(T[2])
        T[1] = new
        T[2] = delete(T[2], new)
    return T

def path_to_largest(T):
    path = []
    if T is None:
        return path
    path.append(T[1])
    return path+path_to_largest(T[2])

# ******************** LAB RESULTS DISPLAY ************************
# Be careful when changing this
if __name__ == "__main__":
    # This is the array we will be using to generate the BST
    A =[11, 6, 7, 16, 17, 2, 4, 18, 14, 8, 15, 1, 20, 13]             

    Test1 =[]             
    Test2 =[1]             
    Test3 =[6, 7, 16, 17, 2, 4, 18, 14, 8, 15, 1, 20, 13]             
    Test4 =[1,2,3,4,5,6,7,8,9]             

    
    # Close all the previously opened figures
    plt.close('all')
    
    # T will be the BST created using our lab functions we need to implement
    # T1 will be a BST created using bst.py so we can compare against if we want to
    T = None
    T1 = bst.BST()
    
    T2 = None
    BST2 = bst.BST()
    
    T3 = None
    BST3 = bst.BST()
    
    T4 = None
    BST4 = bst.BST()
    
    T5 = None
    BST5 = bst.BST()

    # Insert all the numbers from the array A to both BSTs
    for item in A:
        print('Inserting', item)
        T1.insert(item)
        T = insert(T, item)   
    print('T=', T)    

    for item in Test1:
        BST2.insert(item)
        T2 = insert(T2, item)
          
    for item in Test2:
        BST3.insert(item)
        T3 = insert(T3, item) 
         
    for item in Test3:
        BST4.insert(item)
        T4 = insert(T4, item)  
        
    for item in Test4:
        BST5.insert(item)
        T5 = insert(T5, item)   
    
    # Compare our in_order against bst.py's in_order
    print("[lab1_bst_list.py] in_order")
    in_order(T)
    print()

    print("[bst.py] in_order")
    T1.in_order()

    # Compare our draw_list_bst against bst.py's draw
    draw_list_bst(T, 'Draw List BST', 'fig_draw_list_bst.png')

    T1.draw()
    print()
    
    BST2.draw()
    BST3.draw()
    BST4.draw()
    BST5.draw()

    
    # Now let's test the other functions
    # This is the place where you will write your own test-cases
    print('leaves =', leaves(T))
    print('size =', size(T))
    print('minimum =', minimum(T))
    print('maximum =', maximum(T))
    print('height =', height(T))
    print('in_tree =', in_tree(T,1))
    print('print_by_level =', print_by_level(T))
    print('items_at_depth_d =', items_at_depth_d(T,1))
    print('depth_of_k =', depth_of_k(T,1))
    print('tree_to_list_stack =', tree_to_list_stack(T))
    print('is_full =', is_full(T))
    print('is_perfect =', is_perfect(T))
    print('delete =', delete(T,11))
    print('path_to_largest =', path_to_largest(T))

    