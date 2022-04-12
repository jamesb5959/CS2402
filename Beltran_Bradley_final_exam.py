import numpy as np
import matplotlib.pyplot as plt
import math
import bst
import btree
from heaps_exercise_1_start import L
import min_heap
import graph_AL
import graph_AM
import dsf

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
    
def reverse_diagonal(A):
    #O(n)
    l=[]
    for i in range(1,len(A)):
        l.append(A[-i][-i])
    l.append(A[0][0])
    for i in range(len(A)):
        A[i][i]=l[i]
    return A
    
def digit_list(n):
    #O(log(n))
    l=[]
    for i in str(n):
        l.append(int(i))
    return l
  
def is_right_child(T,a,b):
    #O(1)
    if T.find(b,return_parent=True)[1]==None:
        return False
    return T.find(b,return_parent=True)[0].key==a
    
def sum_leaves(T):
    #O(n log(n))
    L=[]
    data=0
    for i in T.data:
        data+=i
    L.append([data])
    for i in T.child:
        data=0
        for j in i.data:
            data+=j
        L.append([data])
    
    return L

def combined_words(W):
    #O(n^2)
    L=[]
    S1 = set(W)
    for i in S1:
        for j in S1:
            if i+j in S1:
                L.append(i+j)
    return L

def first_and_last(W):
    #O(n)
    D ={}
    for i in W:
        f=subString=i[0:1]
        l=subString=i[-1]
        if f+l not in D:
            D[f+l]= i
        else:
            D[f+l] += " "+i
    
    return D

def sorted_list_from_heaps(H1,H2):
    #O(n)
    L=[]
    for i in range(len(H1.heap)):
        L.append(H1.heap[i].key)
    for i in range(len(H2.heap)):
        L.append(H2.heap[i].key)
    return sorted(L)

def dsf_AL(S):
    #O(n)
    L=S.set_list()
    G = graph_AL.Graph(len(L))
    #for i in len(L):
     # G.insert_edge(S[i][0],S[i][1])
    return G

def triangle(G,u,v,w):
    #O(n)
    L=[]
    L.append(u)
    L.append(v)
    L.append(w)
    for vert in L:
        for edge in G.AL[vert]:
            if vert is u and edge.dest != v:
                return False
            if vert is v and edge.dest != w:
                return False
            if vert is w and edge.dest != u:
                return False
    return True

def is_complete(G):
    #O(n^2)
    for u in range(G.AM.shape[0]):
      for v in range(G.AM.shape[1]):
          if G.AM[u][v] != G.AM[v][u]:
              return False 
    return True
    

if __name__ == "__main__":

    plt.close("all")
    S=dsf.DSF(4)
    S.parent=[1,-1,1,2]
    g = dsf_AL(S)
    g.draw()

    print('================ Question 1 ===============')
    np.random.seed(0)
    for i in range(4,7):
        print('Original array')
        A = np.random.randint(0,20,size=(i,i))
        print(A)
        reverse_diagonal(A)
        print('Array with diagonal reversed')
        print(A)

    print('================ Question 2 ===============')
    for n in [6,43,147,2302,10710]:
        print(digit_list(n))

    print('================ Question 3 ===============')

    T = build_BST_from_list([6,  12, 22, 20, 24, 18,  8, 2,  4, 10, 1 ,5,3,7])
    T.draw('question 3')
    a, b = 6, 12
    print('is_right_child(T,{},{}) = {}'.format(a,b,is_right_child(T,a,b)))
    a, b = 10, 11
    print('is_right_child(T,{},{}) = {}'.format(a,b,is_right_child(T,a,b)))
    a, b = 2, 4
    print('is_right_child(T,{},{}) = {}'.format(a,b,is_right_child(T,a,b)))
    a, b = 8,9
    print('is_right_child(T,{},{}) = {}'.format(a,b,is_right_child(T,a,b)))
    
    
    print('================ Question 4 ===============')
    T = build_BTree_from_list([15,19,5,6,0])
    T.draw('question 4a')
    print(sum_leaves(T))
    T = build_BTree_from_list([15,19,5,6,14,13,10,8,3,1,11,18,4,9,2,20])
    T.draw('question 4b')
    print(sum_leaves(T))
    T = build_BTree_from_list([15,19,5,6,0,7,17,16,12,14,13,10,8,3,1,11,18,4,9,2,20])
    T.draw('question 4c')
    print(sum_leaves(T))
    
    print('================ Question 5 ===============')
    W0 = ['tennis','baseball','golf','racquet','bat','base','glove','ball']
    W1 = ['a','an','the','deter','bat','aside','base','glove','determiner','miner','side']
    W2 =['hold', 'sled', 'want', 'dog', 'ed', 'the', 'sleddog', 'dogsled', 'wanted', 'were', 
         'were', 'werewolf','wolf', 'with', 'withold']
    for W in [W0,W1,W2]:
        print(combined_words(W))

    print('================ Question 6 ===============')
    D = first_and_last(set(W0+W1+W2))
    print(D)
    
    print('================ Question 7 ===============')
    L1 = [32,4,8,16,2]
    L2 = [13, 6, 7]
    L3 = [15,19,5,6,0,7]
    L4 = [25,30]
    for La in [L1,L2]:
        for Lb in [L3,L4]:
            H1 = min_heap.min_heap()
            H2 = min_heap.min_heap()
            for i in La:
                H1.insert(i)
            for j in Lb:
                H2.insert(j)
            print(sorted_list_from_heaps(H1,H2))
    
    print('================ Question 8 ===============')
    s = dsf.DSF(7)
    s.union(0,1)
    s.union(4,2)
    s.union(3,5)
    s.union(1,5)
    s.draw('question 8')
    g = dsf_AL(s)
    g.draw('question 8')
    g.display()

    print('================ Question 9 ===============')
    g = graph_AL.Graph(6,directed=True)
    g.insert_edge(0,2)
    g.insert_edge(4,0)
    g.insert_edge(1,3)
    g.insert_edge(3,5)
    g.insert_edge(5,1)
    g.insert_edge(2,5)
    g.insert_edge(1,2)
    g.insert_edge(5,0)
    g.insert_edge(5,1)
    g.insert_edge(1,4)
    g.insert_edge(2,4)

    g.draw('question 9')
    for u in [0,1]:
        for v in [2,3]:
            for w in [4,5]:
                print(u,v,w,triangle(g,u,v,w))

    print('================ Question 10 ===============')
    g1 = graph_AM.Graph(4)
    for i in range(4):
        for j in range(i):
            g1.insert_edge(i,j)
    g2 = graph_AM.Graph(6)
    g2.insert_edge(1,2)
    g2.insert_edge(1,3)
    g2.insert_edge(0,3)
    g2.insert_edge(3,2)
    g2.insert_edge(3,4)
    g2.insert_edge(2,5)
    g2.insert_edge(5,1)
    g1.draw('question 10')
    g2.draw('question 10')
    print(is_complete(g1))
    print(is_complete(g2))

'''
================ Question 1 ===============
Original array
[[12 15  0  3]
 [ 3  7  9 19]
 [18  4  6 12]
 [ 1  6  7 14]]
Array with diagonal reversed
[[14 15  0  3]
 [ 3  6  9 19]
 [18  4  7 12]
 [ 1  6  7 12]]
Original array
[[17  5 13  8  9]
 [19 16 19  5 15]
 [15  0 18  3 17]
 [19 19 19 14  7]
 [ 0  1  9  0 10]]
Array with diagonal reversed
[[10  5 13  8  9]
 [19 14 19  5 15]
 [15  0 18  3 17]
 [19 19 19 16  7]
 [ 0  1  9  0 17]]
Original array
[[ 3 11 18  2  0  0]
 [ 4  5  6  8 17 15]
 [ 4  9 10  1  1  7]
 [ 9  3  6 11 14 18]
 [ 0 14  3 12 10 11]
 [ 4  6  4 15  3 12]]
Array with diagonal reversed
[[12 11 18  2  0  0]
 [ 4 10  6  8 17 15]
 [ 4  9 11  1  1  7]
 [ 9  3  6 10 14 18]
 [ 0 14  3 12  5 11]
 [ 4  6  4 15  3  3]]
================ Question 2 ===============
[6]
[4, 3]
[1, 4, 7]
[2, 3, 0, 2]
[1, 0, 7, 1, 0]
================ Question 3 ===============
is_right_child(T,6,12) = True
is_right_child(T,10,11) = False
is_right_child(T,2,4) = True
is_right_child(T,8,9) = False
================ Question 4 ===============
[45]
[6, 11, 43, 72]
[3, 9, 24, 23, 29, 74]
================ Question 5 ===============
{'baseball'}
{'aside', 'determiner'}
{'werewolf', 'dogsled', 'sleddog', 'wanted'}
================ Question 6 ===============
{'bl': ['ball', 'baseball'], 'rt': ['racquet'], 'ae': ['aside'], 'wd': ['withold', 'wanted'], 'dg': ['dog'], 'gf': ['golf'], 'dd': ['dogsled'], 'wf': ['werewolf', 'wolf'], 'wh': ['with'], 'aa': ['a'], 'hd': ['hold'], 'we': ['were'], 'bt': ['bat'], 'te': ['the'], 'dr': ['deter', 'determiner'], 'be': ['base'], 'an': ['an'], 'ge': ['glove'], 'wt': ['want'], 'se': ['side'], 'sd': ['sled'], 'ed': ['ed'], 'ts': ['tennis'], 'mr': ['miner'], 'sg': ['sleddog']}
================ Question 7 ===============
[0, 2, 4, 5, 6, 7, 8, 15, 16, 19, 32]
[2, 4, 8, 16, 25, 30, 32]
[0, 5, 6, 6, 7, 7, 13, 15, 19]
[6, 7, 13, 25, 30]
================ Question 8 ===============
Graph representation
directed: True, weighted: False
Adjacency list:
AL[0]=[(1,1)]
AL[1]=[(5,1)]
AL[2]=[]
AL[3]=[(5,1)]
AL[4]=[(2,1)]
AL[5]=[]
AL[6]=[]
================ Question 9 ===============
0 2 4 True
0 2 5 True
0 3 4 False
0 3 5 False
1 2 4 False
1 2 5 True
1 3 4 False
1 3 5 True
================ Question 10 ===============
True
False
'''