import numpy as np
import matplotlib.pyplot as plt
import dsf
import graph_AL
import min_heap
import math

def random_graph(nv,ne,weighted=False, directed = False,seed=-1):
    if seed>=0:
        np.random.seed(seed)
    G=graph_AL.Graph(nv,weighted=weighted, directed = directed)
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

def dijkstra(G,source=0):
    visited = set()
    dist  = [math.inf for v in G.AL]
    prev  = [-1 for v in G.AL]
    dist[source] = 0
    H = min_heap.min_heap()
    H.insert(min_heap.heap_record(0,source))
    while len(H.heap)>0 and len(visited)<len(G.AL):
        # if trace: H.draw() # Uncoment it to draw heap at evey step
        v = H.extract_min().data
        if v not in visited and dist[v] != math.inf:
            visited.add(v)
            for edge in G.AL[v]:
                alt_dist = dist[v] + edge.weight
                if alt_dist < dist[edge.dest]: # Path going through v is shorter than previously found path
                    dist[edge.dest] = alt_dist
                    prev[edge.dest] = v
                    H.insert(min_heap.heap_record(alt_dist,edge.dest))
    return prev,dist

def in_degrees(G):
    L = [0 for i in range(len(G.AL))]
    for vert in G.AL:
        for edge in vert:
            L[edge.dest] +=1
    return L

def connected(G,u,v):
    # T(V,E) = O(|V|*|E|)
    S = dsf.DSF(len(G.AL))
    for i in range(len(G.AL)):
        for j in G.AL[i]:
            S.union(i, j.dest)
    return S.in_same_set(u, v)
                
def breadth_first_search_order(G,source=0):
    # T(V,E) = O(|V|*|E|)
    visited_list = [source]
    Q = [source]
    while len(Q)>0:
        for edge in G.AL[Q.pop(0)]:
            if edge.dest not in visited_list:
                visited_list.append(edge.dest)
                Q.append(edge.dest)
    return visited_list

def depth_first_search_order(G,source=0,visited=None,prev=None,visited_list=None):
    # T(V,E) = O(|V|*|E|)
    if visited==None:
        visited = set()
        prev = [-1 for i in range(len(G.AL))]
        visited_list=[source]
    visited.add(source)
    for edge in G.AL[source]:
        if edge.dest not in visited:
            prev[edge.dest] = source
            visited_list.append(edge.dest)
            depth_first_search_order(G,edge.dest,visited,prev,visited_list)
    return visited_list

def make_ts(G):
    # T(V,E) = O(|V|*|E|)
    in_deg = np.array(in_degrees(G))
    ts = []
    Q = [i for i in range(len(in_deg)) if in_deg[i]==0]
    while len(Q) != 0:
        v = Q.pop(0)
        ts.append(v)
    for edge in G.AL[v]:
        u = edge.dest
        in_deg[u] -= 1
        if in_deg[u] == 0:
            Q.enqueue(edge)
    if ts == v: 
        return ts
    else:
        return None

def find_dist(G,prev,u):
    # T(V,E) = O(|V|*|E|) 
    source,dest = prev[u],u
    dist = 0
    while source != -1:
        for edge in G.AL[source]:
            if edge.dest == dest:
                dest = source
                source = prev[dest]
                dist = dist+edge.weight
    return dist

if __name__ == "__main__":
    plt.close("all")

    print('\nQuestion 1')
    v_n, e_n = 8, 5
    np.random.seed(0)
    G1 = random_graph(v_n, e_n)
    G1.display('G1')
    G1.draw('G1')
    for u in range(v_n):
        for v in range(u+1, v_n):
            print('connected(G1,{},{}) = {}'.format(u,v,connected(G1,u,v)))

    print('\nQuestion 2')
    for i in range(1):
        v_n, e_n = 7,12
        np.random.seed(i)
        G2 = random_graph(v_n, e_n,directed=True)
        G2.draw('G2')
        G2.display('G2')
        for source in range(v_n):
            visited_list = breadth_first_search_order(G2,source)
            print('source =',source, 'breadth-first search order', visited_list)

    print('\nQuestion 3')
    for i in range(1):
        v_n, e_n = 7,12
        np.random.seed(i)
        G3 = random_graph(v_n, e_n,directed=True)
        G3.draw('G3')
        G3.display('G3')
        for source in range(v_n):
            visited_list = depth_first_search_order(G3,source)
            print('source =',source, 'depth-first search order', visited_list)

    print('\nQuestion 4')
    for i in range(1):
        v_n, e_n = 7,11
        np.random.seed(i)
        G4 = random_graph(v_n, e_n,directed=True)
        G4.draw('G4')
        G4.display('G4')
        s = make_ts(G4)
        print('Topological sort:',s)
        G4.draw('G4 after removing edges (if necessary)')
        G4.display('G4 after removing edges (if necessary)')

    print('\nQuestion 5')
    for i in range(1):
        np.random.seed(i)
        G5 = random_graph(7,12,directed=True,weighted=True)
        G5.display('G5')
        G5.draw('G5')
        prev,dist = dijkstra(G5)
        print('Results:')
        print('prev = ',prev)
        print('dist = ',dist)
        print('Distances')
        for v in range(len(G5.AL)):
            print(v,find_dist(G5,prev,v))

'''
Question 1
G1 representation
directed: False, weighted: False
Adjacency list:
AL[0]=[(4,1)]
AL[1]=[(7,1), (3,1)]
AL[2]=[(4,1)]
AL[3]=[(1,1), (7,1)]
AL[4]=[(0,1), (2,1)]
AL[5]=[]
AL[6]=[]
AL[7]=[(1,1), (3,1)]
connected(G1,0,1) = False
connected(G1,0,2) = True
connected(G1,0,3) = False
connected(G1,0,4) = True
connected(G1,0,5) = False
connected(G1,0,6) = False
connected(G1,0,7) = False
connected(G1,1,2) = False
connected(G1,1,3) = True
connected(G1,1,4) = False
connected(G1,1,5) = False
connected(G1,1,6) = False
connected(G1,1,7) = True
connected(G1,2,3) = False
connected(G1,2,4) = True
connected(G1,2,5) = False
connected(G1,2,6) = False
connected(G1,2,7) = False
connected(G1,3,4) = False
connected(G1,3,5) = False
connected(G1,3,6) = False
connected(G1,3,7) = True
connected(G1,4,5) = False
connected(G1,4,6) = False
connected(G1,4,7) = False
connected(G1,5,6) = False
connected(G1,5,7) = False
connected(G1,6,7) = False

Question 2
G2 representation
directed: True, weighted: False
Adjacency list:
AL[0]=[(2,1), (5,1), (4,1)]
AL[1]=[(5,1), (0,1)]
AL[2]=[(4,1)]
AL[3]=[(0,1)]
AL[4]=[(5,1), (3,1), (1,1)]
AL[5]=[(6,1)]
AL[6]=[(0,1)]
source = 0 breadth-first search order [0, 2, 5, 4, 6, 3, 1]
source = 1 breadth-first search order [1, 5, 0, 6, 2, 4, 3]
source = 2 breadth-first search order [2, 4, 5, 3, 1, 6, 0]
source = 3 breadth-first search order [3, 0, 2, 5, 4, 6, 1]
source = 4 breadth-first search order [4, 5, 3, 1, 6, 0, 2]
source = 5 breadth-first search order [5, 6, 0, 2, 4, 3, 1]
source = 6 breadth-first search order [6, 0, 2, 5, 4, 3, 1]

Question 3
G3 representation
directed: True, weighted: False
Adjacency list:
AL[0]=[(2,1), (5,1), (4,1)]
AL[1]=[(5,1), (0,1)]
AL[2]=[(4,1)]
AL[3]=[(0,1)]
AL[4]=[(5,1), (3,1), (1,1)]
AL[5]=[(6,1)]
AL[6]=[(0,1)]
source = 0 depth-first search order [0, 2, 4, 5, 6, 3, 1]
source = 1 depth-first search order [1, 5, 6, 0, 2, 4, 3]
source = 2 depth-first search order [2, 4, 5, 6, 0, 3, 1]
source = 3 depth-first search order [3, 0, 2, 4, 5, 6, 1]
source = 4 depth-first search order [4, 5, 6, 0, 2, 3, 1]
source = 5 depth-first search order [5, 6, 0, 2, 4, 3, 1]
source = 6 depth-first search order [6, 0, 2, 4, 5, 3, 1]

Question 4
G4 representation
directed: True, weighted: False
Adjacency list:
AL[0]=[(2,1), (5,1), (4,1)]
AL[1]=[(5,1), (0,1)]
AL[2]=[(4,1)]
AL[3]=[(0,1)]
AL[4]=[(5,1), (3,1), (1,1)]
AL[5]=[]
AL[6]=[(0,1)]
deleting edge (4,1)
deleting edge (3,0)
Topological sort: [6, 1, 0, 2, 4, 5, 3]
G4 after removing edges (if necessary) representation
directed: True, weighted: False
Adjacency list:
AL[0]=[(2,1), (5,1), (4,1)]
AL[1]=[(5,1), (0,1)]
AL[2]=[(4,1)]
AL[3]=[]
AL[4]=[(5,1), (3,1)]
AL[5]=[]
AL[6]=[(0,1)]

Question 5
G5 representation
directed: True, weighted: True
Adjacency list:
AL[0]=[(2,1), (5,6), (4,2)]
AL[1]=[(5,8), (0,9)]
AL[2]=[(4,3)]
AL[3]=[(0,5)]
AL[4]=[(5,10), (3,11), (1,4)]
AL[5]=[(6,12)]
AL[6]=[(0,7)]
Results:
prev =  [-1, 4, 0, 4, 0, 0, 5]
dist =  [0, 6, 1, 13, 2, 6, 18]
Distances
0 0
1 6
2 1
3 13
4 2
5 6
6 18
'''
