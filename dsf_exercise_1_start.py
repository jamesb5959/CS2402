import matplotlib.pyplot as plt
import numpy as np
import dsf
import math

def make_dsf(pairs):
    #O(|V|)
    n = max([p[0] for p in pairs]+[p[1] for p in pairs])+1
    S = dsf.DSF(n)
    for p in pairs:
        S.union(p[0],p[1])
    return S

def is_root(S,a):
    return a == S.find(a)

def is_leaf(S,a):
    if a==S.find(a):
        return False
    if S.find(a) > S.parent[a]:
        return True
    return True

def is_singleton(S,a):
    if -1 == S.parent[a]:
        return True
    return False
if __name__=="__main__":

    plt.close('all')

    P1 = [[5,0],[8,7],[1,4],[4,5],[3,7]]
    P2 = [[3,0],[3,4],[3,1],[6,7],[7,2]]

    print('\nQuestion 1')
    for P in [P1,P2]:
        print('P=',P)
        S = make_dsf(P)
        print('S.parent =',S.parent)
        print('List of sets =',S.set_list())
        S.draw()

    print('\nQuestion 2')
    for P in [P1,P2]:
        S = make_dsf(P)
        S.draw('DSF for questions 2, 3, and 4')
        print('S.parent =',S.parent)
        for i in range(len(S.parent)):
            print('is_root(S,{}) = {}'.format(i,is_root(S,i)))

    print('\nQuestion 3')
    for P in [P1,P2]:
        S = make_dsf(P)
        print('S.parent =',S.parent)
        for i in range(len(S.parent)):
            print('is_leaf(S,{}) = {}'.format(i,is_leaf(S,i)))

    print('\nQuestion 4')
    for P in [P1,P2]:
        S = make_dsf(P)
        print('S.parent =',S.parent)
        for i in range(len(S.parent)):
            print('is_singleton(S,{}) = {}'.format(i,is_singleton(S,i)))

'''
Question 1
P= [[5, 0], [6, 7], [1, 4], [4, 5], [3, 7]]
S.parent = [-4, 4, -1, 7, 0, 0, 7, -3]
List of sets = [{0, 1, 4, 5}, {2}, {3, 6, 7}]
P= [[5, 0], [3, 4], [3, 1], [6, 7], [7, 2]]
S.parent = [-2, 4, 7, 4, -3, 0, 7, -3]
List of sets = [{0, 5}, {1, 3, 4}, {2, 6, 7}]

Question 2
S.parent = [-4, 4, -1, 7, 0, 0, 7, -3]
is_root(S,0) = True
is_root(S,1) = False
is_root(S,2) = True
is_root(S,3) = False
is_root(S,4) = False
is_root(S,5) = False
is_root(S,6) = False
is_root(S,7) = True
S.parent = [-2, 4, 7, 4, -3, 0, 7, -3]
is_root(S,0) = True
is_root(S,1) = False
is_root(S,2) = False
is_root(S,3) = False
is_root(S,4) = True
is_root(S,5) = False
is_root(S,6) = False
is_root(S,7) = True

Question 3
S.parent = [-4, 4, -1, 7, 0, 0, 7, -3]
is_leaf(S,0) = False
is_leaf(S,1) = True
is_leaf(S,2) = True
is_leaf(S,3) = True
is_leaf(S,4) = False
is_leaf(S,5) = True
is_leaf(S,6) = True
is_leaf(S,7) = False
S.parent = [-2, 4, 7, 4, -3, 0, 7, -3]
is_leaf(S,0) = False
is_leaf(S,1) = True
is_leaf(S,2) = True
is_leaf(S,3) = True
is_leaf(S,4) = False
is_leaf(S,5) = True
is_leaf(S,6) = True
is_leaf(S,7) = False

Question 4
S.parent = [-4, 4, -1, 7, 0, 0, 7, -3]
is_singleton(S,0) = False
is_singleton(S,1) = False
is_singleton(S,2) = True
is_singleton(S,3) = False
is_singleton(S,4) = False
is_singleton(S,5) = False
is_singleton(S,6) = False
is_singleton(S,7) = False
S.parent = [-2, 4, 7, 4, -3, 0, 7, -3]
is_singleton(S,0) = False
is_singleton(S,1) = False
is_singleton(S,2) = False
is_singleton(S,3) = False
is_singleton(S,4) = False
is_singleton(S,5) = False
is_singleton(S,6) = False
is_singleton(S,7) = False

runfile('C:/Users/ofuentes/OneDrive - University of Texas at El Paso/CS2302/Part 4/exercises/dsf_exercise_1_solution.py', wdir='C:/Users/ofuentes/OneDrive - University of Texas at El Paso/CS2302/Part 4/exercises')
Reloaded modules: dsf

Question 1
P= [[5, 0], [8, 7], [1, 4], [4, 5], [3, 7]]
S.parent = [-4, 4, -1, 7, 0, 0, -1, -3, 7]
List of sets = [{0, 1, 4, 5}, {2}, {6}, {8, 3, 7}]
P= [[3, 0], [3, 4], [3, 1], [6, 7], [7, 2]]
S.parent = [-4, 0, 7, 0, 0, -1, 7, -3]
List of sets = [{0, 1, 3, 4}, {5}, {2, 6, 7}]

Question 2
S.parent = [-4, 4, -1, 7, 0, 0, -1, -3, 7]
is_root(S,0) = True
is_root(S,1) = False
is_root(S,2) = True
is_root(S,3) = False
is_root(S,4) = False
is_root(S,5) = False
is_root(S,6) = True
is_root(S,7) = True
is_root(S,8) = False
S.parent = [-4, 0, 7, 0, 0, -1, 7, -3]
is_root(S,0) = True
is_root(S,1) = False
is_root(S,2) = False
is_root(S,3) = False
is_root(S,4) = False
is_root(S,5) = True
is_root(S,6) = False
is_root(S,7) = True

Question 3
S.parent = [-4, 4, -1, 7, 0, 0, -1, -3, 7]
is_leaf(S,0) = False
is_leaf(S,1) = True
is_leaf(S,2) = True
is_leaf(S,3) = True
is_leaf(S,4) = False
is_leaf(S,5) = True
is_leaf(S,6) = True
is_leaf(S,7) = False
is_leaf(S,8) = True
S.parent = [-4, 0, 7, 0, 0, -1, 7, -3]
is_leaf(S,0) = False
is_leaf(S,1) = True
is_leaf(S,2) = True
is_leaf(S,3) = True
is_leaf(S,4) = True
is_leaf(S,5) = True
is_leaf(S,6) = True
is_leaf(S,7) = False

Question 4
S.parent = [-4, 4, -1, 7, 0, 0, -1, -3, 7]
is_singleton(S,0) = False
is_singleton(S,1) = False
is_singleton(S,2) = True
is_singleton(S,3) = False
is_singleton(S,4) = False
is_singleton(S,5) = False
is_singleton(S,6) = True
is_singleton(S,7) = False
is_singleton(S,8) = False
S.parent = [-4, 0, 7, 0, 0, -1, 7, -3]
is_singleton(S,0) = False
is_singleton(S,1) = False
is_singleton(S,2) = False
is_singleton(S,3) = False
is_singleton(S,4) = False
is_singleton(S,5) = True
is_singleton(S,6) = False
is_singleton(S,7) = False
'''