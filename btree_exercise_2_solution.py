import btree
import math
import matplotlib.pyplot as plt

def largest_at_depth_d_loop(t,d):
    # T(n) = O(log(n)) - since we follow a path with length at most height(t), 
    # and the tree's height is O(log n)
    for i in range (d):
        if len(t.child)==0:
            return -math.inf
        t = t.child[-1]
    return t.data[-1]

def largest_at_depth_d(t,d):
    # T(n) = T(n/6) + c
    # a=1, b=6, k=0; a==b^k, thus case 2 applies
    # T(n) = O(log(n))
    if d==0:
        return t.data[-1]
    if len(t.child)==0:
        return -math.inf
    return largest_at_depth_d(t.child[-1],d-1)

def find_depth(t,k):
    # Running time is dominated by call to t.find_subtree(k), which has the following recurrence
    # T(n) = T(n/6) + c
    # a=1, b=6, k=0; a==b^k, thus case 2 applies
    # T(n) = O(log(n))
    if k in t.data:
        return 0
    if len(t.child)==0:
        return -1
    i = t.find_subtree(k)
    d = find_depth(t.child[i],k)
    if d>=0:
        d+=1
    return d

def print_at_depth_d(t,d):
    # T(n) = 6 T(n/6) + c
    # a=6, b=6, k=0; a>b^k, thus case 3 applies
    # T(n) = O(n^log_6(6)) = O(n)
    if d==0:
        for item in t.data:
            print(item,end=' ')
    else:
        for c in t.child:
            print_at_depth_d(c,d-1)

def num_leaves(t):
    # T(n) = 6 T(n/6) + c
    # a=6, b=6, k=0; a>b^k, thus case 3 applies
    # T(n) = O(n^log_6(6)) = O(n)
    if len(t.child)==0:
        return 1
    count = 0
    for c in t.child:
        count +=num_leaves(c)
    return count

def full_nodes_at_depth_d(t,d):
    # T(n) = 6 T(n/6) + c
    # a=6, b=6, k=0; a>b^k, thus case 3 applies
    # T(n) = O(n^log_6(6)) = O(n)
    if d==0:
        return int(len(t.data)==t.max_items)
    count = 0
    for c in t.child:
        count += full_nodes_at_depth_d(c,d-1)
    return count

def print_descending(t):
    # T(n) = 6 T(n/6) + c
    # a=6, b=6, k=0; a>b^k, thus case 3 applies
    # T(n) = O(n^log_6(6)) = O(n)
    if len(t.child)==0:
        for d in t.data[::-1]:
            print(d,end=' ')
    else:
        print_descending(t.child[-1])
        for i in range(len(t.data)-1,-1,-1):
            print(t.data[i],end=' ')
            print_descending(t.child[i])

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