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
    w=1            
    for edge in edges:
        if weighted:
            w = np.random.randint(1,10)
        G.insert_edge(edge[0],edge[1],w)
    return G

def random_dsf(size,sets):
    S = dsf.DSF(size)
    if sets>=size:
        return S
    while size>sets:
        size -= S.union(np.random.randint(len(S.parent)),np.random.randint(len(S.parent)))
    return S

def erase_adjacent_AM(G,v):
    # T(V,E) + O(|V|)
    G.AM[v] = -1
    G.AM[:,v] = -1 

def make_weighted_AL(G):
    # T(V,E) + O(|V|+|E|)
    G.weighted=True
    for v in range(len(G.AL)):
        for edge in G.AL[v]:
            edge.weight = v+edge.dest

def largest_set(S):
    # T(n) = O(n)
    L = S.set_list()
    return L[np.argmax(np.array([len(s) for s in L]))]

def path_2_AM(G,u,v):
    # T(V,E) + O(|V|)
    for w in range(G.AM.shape[0]):
        if G.AM[u,w]>0 and G.AM[w,v]>0:
            return w
    return None

def three_layer_graph_AL(a,b,c):
    # T(V,E) + O(|V|^2)
    G = graph_AL.Graph(a+b+c,directed=True)
    for i in range(a):
        for j in range(a,a+b):
            G.insert_edge(i,j)
    for i in range(a,a+b):
        for j in range(a+b,a+b+c):
            G.insert_edge(i,j)
    return G

def singleton_and_rest(n,i):
    # T(n) = O(n)
    S = dsf.DSF(n)
    L = list(np.arange(n))
    L.pop(i)
    for i in L[1:]:
        S.union(L[0],i)
    return S

if __name__ == "__main__":

    plt.close("all")
    plt.rcParams.update({'figure.max_open_warning': 0})
    ds = {True:' directed', False:' undirected'}
    n_tests = [0,2,2,2,1,1,1] 

    question = 1
    print('\nQuestion',question)
    for i in range(n_tests[question]):
        G1 = random_graph(6, 9, rep='AM',seed=question+i+1)
        G1.display('G1 ')
        G1.draw('G1')
        v = np.random.randint(G1.AM.shape[0])
        erase_adjacent_AM(G1,v)
        G1.display('G1 after removing edges adjacent to '+str(v))
        G1.draw('G1 after removing edges adjacent to '+str(v))

    question = 2
    print('\nQuestion',question)
    for i in range(n_tests[question]):
        G2 = random_graph(6, 9, rep='AL',seed=question+i)
        G2.display('G2')
        G2.draw('G2')
        make_weighted_AL(G2)
        G2.display('G2 weighted')
        G2.draw('G2 weighted')
       
    question = 3
    print('\nQuestion',question)
    for i in range(n_tests[question]):
        np.random.seed(question+i)
        S3 = random_dsf(8,3)
        S3.draw('S3')
        print(largest_set(S3))

    question = 4
    print('\nQuestion',question)
    for i in range(n_tests[question]):
        G4 = random_graph(4, 90, rep='AM',seed=question+i+1)
        G4.display('G1 ')
        G4.draw('G4')
        for u in range(4):
            for v in range(u):
                print(u,v,path_2_AM(G4,u,v))
                print(v,u,path_2_AM(G4,v,u))
       
    question = 5
    print('\nQuestion',question)
    for i in range(n_tests[question]):
        np.random.seed(question+i)
        a,b,c = np.random.randint(1,4,size=3)
        print('a={},b={},c={}'.format(a,b,c))
        G5 =  three_layer_graph_AL(a,b,c)
        G5.display('G5')
        G5.draw('G5 a={},b={},c={}'.format(a,b,c))
       
    question = 6
    print('\nQuestion',question)
    for i in range(n_tests[question]):
        np.random.seed(question+i)
        size = np.random.randint(10)
        single = np.random.randint(size)
        S6 = singleton_and_rest(size,single)
        S6.draw('singleton_and_rest({},{})'.format(size,single))
        print(size, single, S6.parent)
        

'''
Question 1
G1  representation
directed: True, weighted: False
Adjacency matrix:
[[-1  1 -1 -1 -1  1]
 [-1 -1 -1 -1 -1 -1]
 [-1  1 -1 -1  1  1]
 [ 1  1 -1 -1  1 -1]
 [-1  1 -1 -1 -1 -1]
 [-1 -1 -1 -1 -1 -1]]
G1 after removing edges adjacent to 1 representation
directed: True, weighted: False
Adjacency matrix:
[[-1 -1 -1 -1 -1  1]
 [-1 -1 -1 -1 -1 -1]
 [-1 -1 -1 -1  1  1]
 [ 1 -1 -1 -1  1 -1]
 [-1 -1 -1 -1 -1 -1]
 [-1 -1 -1 -1 -1 -1]]
G1  representation
directed: True, weighted: False
Adjacency matrix:
[[-1  1 -1 -1  1 -1]
 [-1 -1 -1  1 -1  1]
 [ 1 -1 -1  1  1 -1]
 [-1 -1 -1 -1 -1 -1]
 [-1 -1 -1  1 -1 -1]
 [ 1 -1 -1 -1 -1 -1]]
G1 after removing edges adjacent to 2 representation
directed: True, weighted: False
Adjacency matrix:
[[-1  1 -1 -1  1 -1]
 [-1 -1 -1  1 -1  1]
 [-1 -1 -1 -1 -1 -1]
 [-1 -1 -1 -1 -1 -1]
 [-1 -1 -1  1 -1 -1]
 [ 1 -1 -1 -1 -1 -1]]

Question 2
G2 representation
directed: True, weighted: False
Adjacency list:
AL[0]=[(1,1), (5,1)]
AL[1]=[]
AL[2]=[(1,1), (5,1), (4,1)]
AL[3]=[(0,1), (1,1), (4,1)]
AL[4]=[(1,1)]
AL[5]=[]
G2 weighted representation
directed: True, weighted: True
Adjacency list:
AL[0]=[(1,1), (5,5)]
AL[1]=[]
AL[2]=[(1,3), (5,7), (4,6)]
AL[3]=[(0,3), (1,4), (4,7)]
AL[4]=[(1,5)]
AL[5]=[]
G2 representation
directed: True, weighted: False
Adjacency list:
AL[0]=[(1,1), (4,1)]
AL[1]=[(3,1), (5,1)]
AL[2]=[(0,1), (3,1), (4,1)]
AL[3]=[]
AL[4]=[(3,1)]
AL[5]=[(0,1)]
G2 weighted representation
directed: True, weighted: True
Adjacency list:
AL[0]=[(1,1), (4,4)]
AL[1]=[(3,4), (5,6)]
AL[2]=[(0,2), (3,5), (4,6)]
AL[3]=[]
AL[4]=[(3,7)]
AL[5]=[(0,5)]

Question 3
{0, 1, 2, 3, 5}
{0, 1, 2, 5, 6, 7}

Question 4
G1  representation
directed: True, weighted: False
Adjacency matrix:
[[-1  1  1 -1]
 [-1 -1 -1 -1]
 [-1  1 -1 -1]
 [ 1  1  1 -1]]
1 0 None
0 1 2
2 0 None
0 2 None
2 1 None
1 2 None
3 0 None
0 3 None
3 1 0
1 3 None
3 2 0
2 3 None

Question 5
a=3,b=2,c=3
G5 representation
directed: True, weighted: False
Adjacency list:
AL[0]=[(3,1), (4,1)]
AL[1]=[(3,1), (4,1)]
AL[2]=[(3,1), (4,1)]
AL[3]=[(5,1), (6,1), (7,1)]
AL[4]=[(5,1), (6,1), (7,1)]
AL[5]=[]
AL[6]=[]
AL[7]=[]

Question 6
9 3 [1, -8, 1, -1, 1, 1, 1, 1, 1]
'''
