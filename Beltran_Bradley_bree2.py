# Starter code for B-trees, exercise 2
# rename as lastname_firstname_btree2.py

import btree
import math
import matplotlib.pyplot as plt

def largest_at_depth_d_loop(t,d): 
    # O(log(n)) - since the tree's depth is log n
    while d != 0:
        if len(t.child)==0:
            return -math.inf
        t = t.child[-1]
        d=d-1
    return t.data[-1]

def largest_at_depth_d(t,d):
    # O(log(n)) - since the tree's depth is log n
    # T(n) = T(n/5) + c
    if d==0:
        return t.data[-1]
    if len(t.child)==0:
        return -math.inf
    return largest_at_depth_d(t.child[-1],d-1)

def find_depth(t,k):  
    # T(n) = 5 T(n/5) + c
    # T(n) = O(n)      
    count = -1
    if k in t.data:
        return count+1
    for c in t.child:
        if find_depth(c,k) is not -1:
            count =1+find_depth(c,k)
    return count

def print_at_depth_d(t,d):
    # T(n) = 5 T(n/5) + c
    # T(n) = O(n) 
    if d == 0:
        print(t.data)
    for c in t.child:
        print_at_depth_d(c,d-1)

def num_leaves(t):
    # T(n) = 5 T(n/5) + c
    # T(n) = O(n) 
    count = 0
    if len(t.child)==0:
        return count+1
    for c in t.child:
        if num_leaves(c) != 0:
            count+=num_leaves(c)
    return count

def full_nodes_at_depth_d(t,d):
    # T(n) = 5 T(n/5) + c
    # T(n) = O(n) 
    count = 0
    if d == 0 and t.is_full:
        count += 1
    for c in t.child:
        count += full_nodes_at_depth_d(c,d-1)
    return count

def print_descending(t):
    # T(n) = 5 T(n/5) + c
    # T(n) = O(n) 
    print(t.data)
    for c in t.child:
        print_descending(c)

if __name__ == "__main__":
    plt.close('all')

    T1 = btree.BTree()
    for num in [32,12,58,7,43]:
        T1.insert(num)

    T2 = btree.BTree()
    nums = [6, 3, 23,16, 11, 25, 7, 17,27, 30, 21, 14, 26, 8, 29,
            22, 28, 5, 19, 24, 15, 1, 2, 4, 18, 13, 9, 20, 10, 12]
    for num in nums:
        T2.insert(num)

    T1.draw()
    T2.draw()

    print('Question 1')
    for d in range(2):
        print(d,largest_at_depth_d_loop(T1,d))
    for d in range(4):
        print(d,largest_at_depth_d_loop(T2,d))

    print('Question 2')
    for d in range(2):
        print(d,largest_at_depth_d(T1,d))
    for d in range(4):
        print(d,largest_at_depth_d(T2,d))

    print('Question 3')
    for k in [7, 11, 12, 17, 20, 58]:
        print(find_depth(T1,k))
    for k in [7, 11, 12, 17, 20, 58]:
        print(find_depth(T2,k))

    print('Question 4')
    for d in range(2):
        print_at_depth_d(T1,d)
        print()
    for d in range(4):
        print_at_depth_d(T2,d)
        print()

    print('Question 5')
    print(num_leaves(T1))
    print(num_leaves(T2))

    print('Question 6')
    for d in range(2):
        print(d,full_nodes_at_depth_d(T1,d))
    for d in range(4):
        print(d,full_nodes_at_depth_d(T2,d))

    print('Question 7')
    print_descending(T1)
    print()
    print_descending(T2)
    print()
    
'''
Expected Output:
Question 1
0 58
1 -inf
0 17
1 27
2 30
3 -inf
Question 2
0 58
1 -inf
0 17
1 27
2 30
3 -inf
Question 3
0
-1
0
-1
-1
0
2
1
2
0
2
-1
Question 4
7 12 32 43 58 

17 
6 11 23 27 
1 2 3 4 5 7 8 9 10 12 13 14 15 16 18 19 20 21 22 24 25 26 28 29 30 

Question 5
1
6
Question 6
0 1
1 0
0 0
1 0
2 3
3 0
Question 7
58 43 32 12 7 
30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 
'''