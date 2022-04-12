import numpy as np
import math
import matplotlib.pyplot as plt
import graph_AM
import graph_AL
import dsf

def random_graph(nv,ne,weighted=False, directed = True,seed=-1,rep='AL'):
    if seed>=0:
        np.random.seed(seed)
    if rep == 'AL':
        G=graph_AL.Graph(nv,weighted=weighted, directed = directed)
    else:
        G=graph_AM.Graph(nv,weighted=weighted, directed = directed)
    edges = set()
    ne = min(ne,nv*(nv-1)//2)
    while len(edges) < ne:
        source = np.random.randint(nv)
        dest = (np.random.randint(1,nv)+source)%nv
        if (source,dest) not in edges and (dest,source) not in edges:
            edges.add((source,dest))
    if weighted:
        w = np.random.permutation(ne) + 1
    else:
        w = np.ones(ne,dtype=np.int32)
    for i, edge in enumerate(edges):
        G.insert_edge(edge[0],edge[1],w[i])
    return G

def random_dsf(size,sets):
    S = dsf.DSF(size)
    if sets>=size:
        return S
    while size>sets:
        size -= S.union(np.random.randint(len(S.parent)),np.random.randint(len(S.parent)))
    return S

def sum_weights_AM(G,v):
    # T(V,E) = O(|V|)
    sum = 0
    for e in range(G.AM.shape[0]):
        if G.AM[v][e] != -1:
            sum += G.AM[v][e]
        if G.AM[e][v] != -1:
            sum += G.AM[e][v]
    return sum

def make_unweighted_AL(G):
    # T(V,E) = O(|E|)
    G.weighted=False

def count_singletons(S):
    # T(n) = O(n)
    count = 0
    SL=S.set_list()
    for i in range(len(SL)):
        if S.union(-1, i) == 0:
            count+=1
    return count

def clique3_AM(G,u,v,x):
    # T(V,E) = O(|V|)
    for e in range(G.AM.shape[0]):
        if G.AM[u,e]>0 and G.AM[e,v]>0 and G.AM[e,x]>0:
            return False
    return True

def highest_weight_edge(G):
    # T(V,E) = O(|E|+|V|)
    biggest = [0,0,-math.inf]
    if G.weighted==False:
        return biggest
    for v in range(G.vertices):
        for e in G.AL[v]:
            if e.weight > biggest[2]:
                biggest = [v, e.dest, e.weight]
    return biggest

def in_same_set(S,a,b,c):
    # T(n) = O(1)
    if S.in_same_set(a,b) ==  False or S.in_same_set(a,c) ==  False or S.in_same_set(b,c) ==  False:
        return False  
    return True

if __name__ == "__main__":

    plt.close("all")
    n_tests = [0,1,1,2,1,2,2]

    question = 1
    print('\nQuestion',question)
    for i in range(n_tests[question]):
        G1 = random_graph(5, 4, rep='AM',weighted=True,seed=question+i+1)
        G1.display('G1 ')
        G1.draw('G1')
        for v in range(G1.AM.shape[0]):
            print('sum_weights_AM(G,{}) = {}'.format(v,sum_weights_AM(G1,v)))

    question = 2
    print('\nQuestion',question)
    for i in range(n_tests[question]):
        G2 = random_graph(4, 5, rep='AL',weighted=True, seed=question+i)
        G2.display('G2')
        G2.draw('G2')
        make_unweighted_AL(G2)
        G2.display('G2 unweighted')
        G2.draw('G2 unweighted')

    question = 3
    print('\nQuestion',question)
    for i in range(n_tests[question]):
        np.random.seed(question+i)
        S3 = random_dsf(8,4)
        S3.draw('S3')
        print(S3.parent)
        print('count_singletons(S3)=',count_singletons(S3))

    question = 4
    print('\nQuestion',question)
    for i in range(n_tests[question]):
        G4 = random_graph(5,8, rep='AM',directed=False,seed=question+i)
        G4.display('G4 ')
        G4.draw('G4')
        for x in range(G4.AM.shape[0]):
            for v in range(x):
                for u in range(v):
                    print('clique3_AM(G,{},{},{})={}'.format(u,v,x,clique3_AM(G4,u,v,x)))

    question = 5
    print('\nQuestion',question)
    for i in range(n_tests[question]):
        G5 = random_graph(5, i+5, rep='AL',weighted=True,seed=question+i+2)
        G5.display('G5')
        G5.draw('G5')
        print('highest_weight_edge(G5)=',highest_weight_edge(G5))

    question = 6
    print('\nQuestion',question)
    for i in range(n_tests[question]):
        np.random.seed(question+i)
        S6 = random_dsf(6,2)
        S6.draw('DSF question 6')
        for c in range(len(S6.parent)):
            for b in range(c):
                for a in range(b):
                    print('in_same_set(S,{},{},{})={}'.format(a,b,c,in_same_set(S6,a,b,c)))
        print()


'''
Question 1
G1  representation
directed: True, weighted: True
Adjacency matrix:
[[-1 -1 -1  2  3]
 [-1 -1 -1 -1 -1]
 [-1 -1 -1 -1 -1]
 [-1  1 -1 -1  4]
 [-1 -1 -1 -1 -1]]
sum_weights_AM(G,0) = 5
sum_weights_AM(G,1) = 1
sum_weights_AM(G,2) = 0
sum_weights_AM(G,3) = 7
sum_weights_AM(G,4) = 7

Question 2
G2 representation
directed: True, weighted: True
Adjacency list:
AL[0]=[(1,4), (3,1), (2,3)]
AL[1]=[(3,5)]
AL[2]=[]
AL[3]=[(2,2)]
G2 unweighted representation
directed: True, weighted: False
Adjacency list:
AL[0]=[(1,1), (3,1), (2,1)]
AL[1]=[(3,1)]
AL[2]=[]
AL[3]=[(2,1)]

Question 3
[-5, 3, 0, 0, -1, 0, -1, -1]
count_singletons(S3)= 3
[-4, 0, 6, -1, -1, 0, -2, 5]
count_singletons(S3)= 2

Question 4
G4  representation
directed: False, weighted: False
Adjacency matrix:
[[-1  1  1  1 -1]
 [ 1 -1  1 -1  1]
 [ 1  1 -1  1  1]
 [ 1 -1  1 -1  1]
 [-1  1  1  1 -1]]
clique3_AM(G,0,1,2)=True
clique3_AM(G,0,1,3)=False
clique3_AM(G,0,2,3)=True
clique3_AM(G,1,2,3)=False
clique3_AM(G,0,1,4)=False
clique3_AM(G,0,2,4)=False
clique3_AM(G,1,2,4)=True
clique3_AM(G,0,3,4)=False
clique3_AM(G,1,3,4)=False
clique3_AM(G,2,3,4)=True

Question 5
G5 representation
directed: True, weighted: True
Adjacency list:
AL[0]=[(4,3), (2,2)]
AL[1]=[]
AL[2]=[]
AL[3]=[(4,1), (2,4)]
AL[4]=[(1,5)]
highest_weight_edge(G5)= [4, 1, 5]
G5 representation
directed: True, weighted: True
Adjacency list:
AL[0]=[(2,1)]
AL[1]=[(3,3)]
AL[2]=[(1,4), (3,2)]
AL[3]=[(4,6)]
AL[4]=[(1,5)]
highest_weight_edge(G5)= [3, 4, 6]

Question 6
in_same_set(S,0,1,2)=True
in_same_set(S,0,1,3)=False
in_same_set(S,0,2,3)=False
in_same_set(S,1,2,3)=False
in_same_set(S,0,1,4)=False
in_same_set(S,0,2,4)=False
in_same_set(S,1,2,4)=False
in_same_set(S,0,3,4)=False
in_same_set(S,1,3,4)=False
in_same_set(S,2,3,4)=False
in_same_set(S,0,1,5)=True
in_same_set(S,0,2,5)=True
in_same_set(S,1,2,5)=True
in_same_set(S,0,3,5)=False
in_same_set(S,1,3,5)=False
in_same_set(S,2,3,5)=False
in_same_set(S,0,4,5)=False
in_same_set(S,1,4,5)=False
in_same_set(S,2,4,5)=False
in_same_set(S,3,4,5)=False

in_same_set(S,0,1,2)=True
in_same_set(S,0,1,3)=True
in_same_set(S,0,2,3)=True
in_same_set(S,1,2,3)=True
in_same_set(S,0,1,4)=True
in_same_set(S,0,2,4)=True
in_same_set(S,1,2,4)=True
in_same_set(S,0,3,4)=True
in_same_set(S,1,3,4)=True
in_same_set(S,2,3,4)=True
in_same_set(S,0,1,5)=False
in_same_set(S,0,2,5)=False
in_same_set(S,1,2,5)=False
in_same_set(S,0,3,5)=False
in_same_set(S,1,3,5)=False
in_same_set(S,2,3,5)=False
in_same_set(S,0,4,5)=False
in_same_set(S,1,4,5)=False
in_same_set(S,2,4,5)=False
in_same_set(S,3,4,5)=False
'''
