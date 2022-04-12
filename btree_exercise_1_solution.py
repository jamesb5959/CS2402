import matplotlib.pyplot as plt
import btree
import math
import numpy as np

def height_loop(t):
    # O(log(n)) - since the tree's height is log n
    h = 0
    while len(t.child)>0:
        h+=1
        t = t.child[0]
    return h

def height(t):
    # T(n) = T(n/5) + c
    # T(n) = O(log(n))
    if len(t.child)==0:
        return 0
    return 1 + height(t.child[0])


def smallest_loop(t):
    # O(log(n)) - since the tree's height is log n
    while len(t.child)>0:
        t = t.child[0]
    return t.data[0]

def smallest(t): # Recursive version
    # T(n) = T(n/5) + c
    # T(n) = O(log(n))
    if len(t.child)==0:
        return t.data[0]
    return smallest(t.child[0])

def largest_loop(t):
    # O(log(n)) - since the tree's height is log n
    while len(t.child)>0:
        t = t.child[-1]
    return t.data[-1]

def largest(t): # Recursive version
    # T(n) = T(n/5) + c
    # T(n) = O(log(n))
    if len(t.child)==0:
        return t.data[-1]
    return largest(t.child[-1])

def num_nodes(t):
    # T(n) = 5 T(n/5) + c
    # T(n) = O(n)
    count = 1
    for c in t.child:
        count+= num_nodes(c)
    return count

def num_items(t):
    # T(n) = 5 T(n/5) + c
    # T(n) = O(n)
    count = len(t.data)
    for c in t.child:
        count+= num_items(c)
    return count


if __name__ == "__main__":
    plt.close('all')
    T1 = btree.BTree()
    T2 = btree.BTree()

    nums1 =[38, 56, 14, 42, 32, 60, 52, 68, 20, 10, 24,  0, 40, 46, 44,  8, 48,
       36,  4, 16, 62, 30, 54, 34, 58, 28, 50, 64,  2, 66, 12, 26,  6, 18, 22]

    nums2 =[6, 3, 23, 16, 11, 25, 7, 17, 27, 30, 21, 14, 26, 8, 29, 22, 28]

    for num in nums1:
        T1.insert(num)
    for num in nums2:
        T2.insert(num)

    T1.draw()
    T2.draw()

    print('Question 1')
    print(height_loop(T1))
    print(height_loop(T2))

    print('Question 2')
    print(height(T1))
    print(height(T2))

    print('Question 3')
    print(smallest_loop(T1))
    print(smallest_loop(T2))

    print('Question 4')
    print(smallest(T1))
    print(smallest(T2))

    print('Question 5')
    print(largest_loop(T1))
    print(largest_loop(T2))

    print('Question 6')
    print(largest(T1))
    print(largest(T2))

    print('Question 7')
    print(num_nodes(T1))
    print(num_nodes(T2))

    print('Question 8')
    print(num_items(T1))
    print(num_items(T2))

'''
# Expected results
Question 1
2
1
Question 2
2
1
Question 3
0
3
Question 4
0
3
Question 5
68
30
Question 6
68
30
Question 7
11
5
Question 8
35
17
'''