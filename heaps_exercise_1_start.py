import matplotlib.pyplot as plt
import numpy as np
import min_heap
import math

def change_key(H,k,m):
#O(1) because we go to the keey and see if it can be changed if not we return
    if H.heap[k].key < 0:
        return -1
    if H.right(k)<len(H.heap):
        if m>H.heap[H.right(k)].key:
            return -1
    if H.left(k)<len(H.heap):
        if m>H.heap[H.left(k)].key:
            return -1
    if k != 0:
        if H.heap[H.parent(k)].key>m:
            return -1
    H.heap[k].key=m
    return 1

def max_diff(H):
    #O(n) because it has a for loop
    max = 0
    for i in range(len(H.heap)):
        if H.right(i)<len(H.heap):
            temp = H.heap[H.right(i)].key - H.heap[i].key
            if temp>max:
                max=temp
        if H.left(i)<len(H.heap):
            temp = H.heap[H.left(i)].key - H.heap[i].key
            if temp>max:
                max=temp
    return max

def less_than_k(H,k):
    #O(n) because it has a for loop
    L = []
    for i in range(len(H.heap)):
        if H.heap[i].key< k:
            L.append(H.heap[i].key)
    return sorted(L)

def extract_from_2_heaps(H1,H2,k) :
    #O(n) because it has a for loop
    L = []
    heapMore=0
    if len(H1.heap)+len(H2.heap)<k:
        heapMore = 1
    for i in range(len(H1.heap)):
        if H1.heap[i].key<= k or heapMore == 1:
            L.append(H1.heap[i].key)
    for i in range(len(H2.heap)):
        if H2.heap[i].key<=k or heapMore == 1:
            L.append(H2.heap[i].key)
    return sorted(L)
#Both less_than_k and extract_from_2_heaps are very confusing

if __name__=="__main__":
    plt.close('all')

    L1 = [5,0,3,7,8,9,14,4,6,8,9,14,5,6,7,6]
    L2 = [13,17,18]
    L3 = [1,2,4,8,14,5,6,7,6]
    L4 = [5,0,3,7,8,9,1,5,6,7,6,13]

    H =  min_heap.min_heap()
    for i in L1:
        H.insert(i)
    H.draw(indices=True)

    print('Question 1')
    ch = change_key(H,0,4)
    print(ch)
    if ch ==1:
        print('Heap was modified')
        H.draw('New heap')
    else:
        print('Heap could not be changed witout violating heap property')

    ch = change_key(H,7,8)
    print(ch)
    if ch ==1:
        print('Heap was modified')
        H.draw('New heap')
    else:
        print('Heap could not be changed witout violating heap property')

    ch = change_key(H,5,2)
    print(ch)
    if ch ==1:
        print('Heap was modified')
        H.draw('New heap')
    else:
        print('Heap could not be changed witout violating heap property')

    ch = change_key(H,6,8)
    print(ch)
    if ch ==1:
        print('Heap was modified')
        H.draw('New heap')
    else:
        print('Heap could not be changed witout violating heap property')

    ch = change_key(H,4,5)
    print(ch)
    if ch ==1:
        print('Heap was modified')
        H.draw('New heap')
    else:
        print('Heap could not be changed witout violating heap property')

    ch = change_key(H,2,4)
    print(ch)
    if ch ==1:
        print('Heap was modified')
        H.draw('New heap')
    else:
        print('Heap could not be changed witout violating heap property')

    print('Question 2')
    for L in [L1,L2,L3,L4]:
        H = min_heap.min_heap()
        for i in L:
            H.insert(i)
        H.draw('Heap for questions 2 and 3')
        print(max_diff(H))

    print('Question 3')
    for L in [L1,L2,L3,L4]:
        H = min_heap.min_heap()
        for i in L:
            H.insert(i)
        print(less_than_k(H,8))
        print(less_than_k(H,12))

    print('Question 4')
    L1 = [20,1,7,2,8,9,15]
    L2 = [18, 25, 11,6,10,12,13]
    for k in [1,2,4,8,16,32]:
        H1 = min_heap.min_heap()
        for i in L1:
            H1.insert(i)
        H2 = min_heap.min_heap()
        for i in L2:
            H2.insert(i)
        print('k=',k)
        print(extract_from_2_heaps(H1,H2,k))

'''
Question 1
-1
Heap could not be changed witout violating heap property
-1
Heap could not be changed witout violating heap property
-1
Heap could not be changed witout violating heap property
-1
Heap could not be changed witout violating heap property
1
Heap was modified
1
Heap was modified
Question 2
9
5
12
8
Question 3
[0, 3, 4, 5, 5, 6, 6, 6, 7, 7]
[8, 8, 9, 9]
[]
[]
[1, 2, 4, 5, 6, 6, 7]
[8]
[0, 1, 3, 5, 5, 6, 6, 7, 7]
[8, 9]
Question 4
k= 1
[1]
k= 2
[1, 2]
k= 4
[1, 2, 6, 7]
k= 8
[1, 2, 6, 7, 8, 9, 10, 11]
k= 16
[1, 2, 6, 7, 8, 9, 10, 11, 12, 13, 15, 18, 20, 25]
k= 32
[1, 2, 6, 7, 8, 9, 10, 11, 12, 13, 15, 18, 20, 25]
'''