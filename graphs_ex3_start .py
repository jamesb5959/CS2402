import numpy as np
import math
import matplotlib.pyplot as plt
import graph_AM
import graph_AL

def random_graph(nv,ne,weighted=False, directed = False,seed=-1,rep='AL'):
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

def num_edges(G):
    # T(V,E) = O(|E|)
    count = 0
    if type(G) == graph_AL.Graph:
        for i in G.AL:
            count += len(i)
        if not G.directed:
            count=  count//2
        return count
    elif type(G) == graph_AM.Graph:
        count = np.sum(G.AM!=-1)
        if not G.directed:
            count=  count//2
        return count
    return 0

def complement_AL(G):
    # T(V,E) = O(|V|*|E|)
    C = graph_AL.Graph(len(G.AL))
    for v in range(G.vertices):
        for e in G.AL[v]:
            C.insert_edge(v,e.dest)
    return C

def complement_AM(G):
    # T(V,E) = O(|V|*|E|)
    C = graph_AM.Graph(G.AM.shape[0])
    for s in range(len(G.AM)):
        for d in range(len(G.AM[s])):
            if G.AM[s][d] == -1 and s != d:
                C.insert_edge(s, d)
    return C

def remove_left_edges_AL(G):
    # T(V,E) = O(|V|*|E|)
    for i in range(G.vertices-1,-1,-1):
        for j in range(G.vertices-1,-1,-1):
            if i>j:
                G.delete_edge_directed(i,j)
    return G

def remove_left_edges_AM(G):
    # T(V,E) = O(|V|*|E|)
    for i in range(len(G.AM)-1,-1,-1):
        for j in range(len(G.AM[i])-1,-1,-1):
            if i>j:
                G.delete_edge(i,j)
    return G
        
def nearest_neighbor_AL(G,v):
    # T(V,E) = O(|E|)
    nn = -1
    for edge in G.AL[v]:
        nn=edge.dest
        break 
    if nn == -1:
        nn = v-1
    return nn

def nearest_neighbor_AM(G,v):
    # T(V,E) = O(|E|)
    nn=-1
    for i in range(G.AM.shape[0]):
        if G.AM[v][i] != -1:
            nn=i
            break
    if nn == -1:
        nn = v-1
    return nn

def add_vertex_AL(G):
    # T(V,E) = O(|V|)
    return G.AL.append([])

def add_vertex_AM(G):
    # T(V,E) = O(|V|*|E|)
    NG = np.zeros((G.AM.shape[0]+1, G.AM.shape[0]+1),dtype=int)-1
    NG[:-1,:-1] = G.AM
    G.AM=NG
    return G.AM
    
if __name__ == "__main__":

    plt.close("all")
    plt.rcParams.update({'figure.max_open_warning': 0})
    ds = {True:' directed', False:' undirected'}
    tests_per_question = 1 

    print('\nQuestion 1')
    seed = 1
    for R in ['AL','AM']:
        for directed in [False,True]:
            G1 = random_graph(np.random.randint(5,8), np.random.randint(3,10),directed = directed,rep=R,seed=seed)
            G1.display('G1 '+R)
            G1.draw('G1 '+R+ ds[directed])
            print('Number of edges:',num_edges(G1))
            seed+=1

    print('\nQuestion 2')
    for i in range(tests_per_question):
        G2 = random_graph(np.random.randint(5,7), np.random.randint(4,8),rep='AL',seed=i+2)
        G2.display('G2')
        G2.draw('G2')
        CG2 = complement_AL(G2)
        CG2.display('G2 complement')
        CG2.draw('G2 complement')

    print('\nQuestion 3')
    for i in range(tests_per_question):
        G3 = random_graph(np.random.randint(5,7), np.random.randint(4,8),rep='AM',seed=i+3)
        G3.display('G3')
        G3.draw('G3')
        CG3 = complement_AM(G3)
        CG3.display('G3 complement')
        CG3.draw('G3 complement')

    print('\nQuestion 4')
    for i in range(tests_per_question):
        G4 = random_graph(np.random.randint(5,8), np.random.randint(4,10),directed=True, rep='AL',seed=i+4)
        G4.display('G4')
        G4.draw('G4')
        remove_left_edges_AL(G4)
        G4.display('G4 with left edges removed')
        G4.draw('G4 with left edges removed')

    print('\nQuestion 5')
    for i in range(tests_per_question):
        G5 = random_graph(np.random.randint(5,8), np.random.randint(4,10),directed=True, rep='AM',seed=i+5)
        G5.display('G5')
        G5.draw('G5')
        remove_left_edges_AM(G5)
        G5.display('G5 with left edges removed')
        G5.draw('G5 with left edges removed')

    print('\nQuestion 6')
    for i in range(tests_per_question):
        for directed in [False,True]:
            G6 = random_graph(6, 10, directed = directed, weighted=True,rep='AL',seed=i+6)
            G6.display('G6')
            G6.draw('G6'+ ds[directed])
            for v in range(len(G6.AL)):
                print('Nearest neighbor of {} is {}'.format(v,nearest_neighbor_AL(G6,v)))
    
    print('\nQuestion 7')
    for i in range(tests_per_question):
        for directed in [False,True]:
            G7 = random_graph(6, 10, directed = directed, weighted=True,rep='AM',seed=i+7)
            G7.display('G7')
            G7.draw('G7'+ ds[directed])
            for v in range(G7.AM.shape[0]):
                print('Nearest neighbor of {} is {}'.format(v,nearest_neighbor_AM(G7,v)))
            
    print('\nQuestion 8')
    for i in range(tests_per_question):
        G8 = random_graph(5, 9, directed=True, rep='AL',seed=i+8)
        G8.draw('G8')
        G8.display('G8')
        add_vertex_AL(G8)
        G8.display('G8 after adding a vertex')
        G8.draw('G8 after adding a vertex')

    print('\nQuestion 9')
    for i in range(tests_per_question):
        G9 = random_graph(5, 9, directed=True,rep='AM',seed=i+9)
        G9.display('G9')
        G9.draw('G9')
        add_vertex_AM(G9)
        G9.display('G9 after adding a vertex')
        G9.draw('G9 after adding a vertex')
        
'''
Question 1
G1 AL representation
directed: False, weighted: False
Adjacency list:
AL[0]=[(1,1), (4,1)]
AL[1]=[(2,1), (0,1)]
AL[2]=[(1,1)]
AL[3]=[(4,1)]
AL[4]=[(3,1), (0,1)]
Number of edges: 4
G1 AL representation
directed: True, weighted: False
Adjacency list:
AL[0]=[(1,1)]
AL[1]=[]
AL[2]=[(1,1), (4,1)]
AL[3]=[(0,1), (1,1), (4,1)]
AL[4]=[(1,1)]
AL[5]=[]
Number of edges: 7
G1 AM representation
directed: False, weighted: False
Adjacency matrix:
[[-1  1 -1 -1 -1 -1]
 [ 1 -1 -1 -1 -1  1]
 [-1 -1 -1  1 -1 -1]
 [-1 -1  1 -1 -1 -1]
 [-1 -1 -1 -1 -1 -1]
 [-1  1 -1 -1 -1 -1]]
Number of edges: 3
G1 AM representation
directed: True, weighted: False
Adjacency matrix:
[[-1  1 -1  1 -1]
 [-1 -1  1 -1  1]
 [ 1 -1 -1  1 -1]
 [-1 -1 -1 -1 -1]
 [-1 -1  1  1 -1]]
Number of edges: 8

Question 2
G2 representation
directed: False, weighted: False
Adjacency list:
AL[0]=[(1,1), (3,1)]
AL[1]=[(0,1), (3,1), (4,1)]
AL[2]=[(4,1)]
AL[3]=[(0,1), (1,1), (4,1)]
AL[4]=[(3,1), (1,1), (2,1)]
AL[5]=[]
G2 complement representation
directed: False, weighted: False
Adjacency list:
AL[0]=[(2,1), (4,1), (5,1), (2,1), (4,1), (5,1)]
AL[1]=[(2,1), (5,1), (2,1), (5,1)]
AL[2]=[(0,1), (1,1), (0,1), (1,1), (3,1), (5,1), (3,1), (5,1)]
AL[3]=[(2,1), (2,1), (5,1), (5,1)]
AL[4]=[(0,1), (0,1), (5,1), (5,1)]
AL[5]=[(0,1), (1,1), (2,1), (3,1), (4,1), (0,1), (1,1), (2,1), (3,1), (4,1)]

Question 3
G3 representation
directed: False, weighted: False
Adjacency matrix:
[[-1  1  1 -1  1 -1]
 [ 1 -1 -1  1 -1  1]
 [ 1 -1 -1  1 -1 -1]
 [-1  1  1 -1 -1 -1]
 [ 1 -1 -1 -1 -1 -1]
 [-1  1 -1 -1 -1 -1]]
G3 complement representation
directed: False, weighted: False
Adjacency matrix:
[[-1 -1 -1  1 -1  1]
 [-1 -1  1 -1  1 -1]
 [-1  1 -1 -1  1  1]
 [ 1 -1 -1 -1  1  1]
 [-1  1  1  1 -1  1]
 [ 1 -1  1  1  1 -1]]

Question 4
G4 representation
directed: True, weighted: False
Adjacency list:
AL[0]=[(6,1), (5,1), (3,1)]
AL[1]=[(4,1)]
AL[2]=[(1,1), (0,1)]
AL[3]=[]
AL[4]=[(3,1)]
AL[5]=[]
AL[6]=[(1,1), (2,1)]
G4 with left edges removed representation
directed: True, weighted: False
Adjacency list:
AL[0]=[(6,1), (5,1), (3,1)]
AL[1]=[(4,1)]
AL[2]=[]
AL[3]=[]
AL[4]=[]
AL[5]=[]
AL[6]=[]

Question 5
G5 representation
directed: True, weighted: False
Adjacency matrix:
[[-1  1 -1 -1 -1 -1]
 [-1 -1  1 -1 -1 -1]
 [-1 -1 -1 -1 -1 -1]
 [-1 -1 -1 -1  1 -1]
 [ 1 -1  1 -1 -1 -1]
 [-1 -1 -1 -1 -1 -1]]
G5 with left edges removed representation
directed: True, weighted: False
Adjacency matrix:
[[-1  1 -1 -1 -1 -1]
 [-1 -1  1 -1 -1 -1]
 [-1 -1 -1 -1 -1 -1]
 [-1 -1 -1 -1  1 -1]
 [-1 -1 -1 -1 -1 -1]
 [-1 -1 -1 -1 -1 -1]]

Question 6
G6 representation
directed: False, weighted: True
Adjacency list:
AL[0]=[(2,6)]
AL[1]=[(2,3), (4,6), (5,6)]
AL[2]=[(1,3), (3,3), (4,8), (5,9), (0,6)]
AL[3]=[(2,3), (4,3), (5,7)]
AL[4]=[(5,4), (1,6), (3,3), (2,8)]
AL[5]=[(4,4), (1,6), (2,9), (3,7)]
Nearest neighbor of 0 is 2
Nearest neighbor of 1 is 2
Nearest neighbor of 2 is 1
Nearest neighbor of 3 is 2
Nearest neighbor of 4 is 3
Nearest neighbor of 5 is 4
G6 representation
directed: True, weighted: True
Adjacency list:
AL[0]=[(2,6)]
AL[1]=[(2,3), (4,6), (5,6)]
AL[2]=[(4,8), (5,9)]
AL[3]=[(2,3), (5,7)]
AL[4]=[(5,4), (3,3)]
AL[5]=[]
Nearest neighbor of 0 is 2
Nearest neighbor of 1 is 2
Nearest neighbor of 2 is 4
Nearest neighbor of 3 is 2
Nearest neighbor of 4 is 3
Nearest neighbor of 5 is -1

Question 7
G7 representation
directed: False, weighted: True
Adjacency matrix:
[[-1  1  8 -1  1  4]
 [ 1 -1  7  8 -1  8]
 [ 8  7 -1  1 -1  8]
 [-1  8  1 -1  8 -1]
 [ 1 -1 -1  8 -1 -1]
 [ 4  8  8 -1 -1 -1]]
Nearest neighbor of 0 is 1
Nearest neighbor of 1 is 0
Nearest neighbor of 2 is 3
Nearest neighbor of 3 is 2
Nearest neighbor of 4 is 0
Nearest neighbor of 5 is 0
G7 representation
directed: True, weighted: True
Adjacency matrix:
[[-1  1  8 -1 -1  4]
 [-1 -1  7 -1 -1  8]
 [-1 -1 -1  1 -1  8]
 [-1  8 -1 -1 -1 -1]
 [ 1 -1 -1  8 -1 -1]
 [-1 -1 -1 -1 -1 -1]]
Nearest neighbor of 0 is 1
Nearest neighbor of 1 is 2
Nearest neighbor of 2 is 3
Nearest neighbor of 3 is 1
Nearest neighbor of 4 is 0
Nearest neighbor of 5 is -1

Question 8
G8 representation
directed: True, weighted: False
Adjacency list:
AL[0]=[(2,1), (3,1)]
AL[1]=[(3,1), (0,1)]
AL[2]=[(1,1), (3,1)]
AL[3]=[(4,1)]
AL[4]=[(2,1), (1,1)]
G8 after adding a vertex representation
directed: True, weighted: False
Adjacency list:
AL[0]=[(2,1), (3,1)]
AL[1]=[(3,1), (0,1)]
AL[2]=[(1,1), (3,1)]
AL[3]=[(4,1)]
AL[4]=[(2,1), (1,1)]
AL[5]=[]

Question 9
G9 representation
directed: True, weighted: False
Adjacency matrix:
[[-1  1 -1  1  1]
 [-1 -1  1 -1  1]
 [ 1 -1 -1  1 -1]
 [-1 -1 -1 -1 -1]
 [-1 -1  1  1 -1]]
G9 after adding a vertex representation
directed: True, weighted: False
Adjacency matrix:
[[-1  1 -1  1  1 -1]
 [-1 -1  1 -1  1 -1]
 [ 1 -1 -1  1 -1 -1]
 [-1 -1 -1 -1 -1 -1]
 [-1 -1  1  1 -1 -1]
 [-1 -1 -1 -1 -1 -1]]

'''
