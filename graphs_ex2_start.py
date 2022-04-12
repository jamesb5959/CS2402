import numpy as np
import matplotlib.pyplot as plt
import graph_AL
import graph_AM

def neighbors_AL(G,v):
    # T(V,E) =  O(|E|)
    L=[] 
    for edge in G.AL[v]:
        L.append(edge.dest) 
    return L  

def neighbors_AM(G,v):
    # T(V,E) =  O(|E|)
    L=[] 
    for i in range(G.AM.shape[0]):
        if G.AM[v][i] != -1:
            L.append(i)
    return L

def neighbors(G,v):
    # T(V,E) =  O(|E|)
    if type(G) == graph_AL.Graph:
        return neighbors_AL(G,v)
    elif type(G) == graph_AM.Graph:
        return neighbors_AM(G,v)
    print("Not AL or AM")
    
def reversed_edges_AL(G):
    # T(V,E) =  O(|V|+|E|) 
    G1 = graph_AL.Graph(G.vertices,directed=True)
    for v in range(G.vertices):
        for e in G.AL[v]:
            G1.insert_edge(e.dest,v)
    return G1
  
def reversed_edges_AM(G):
    # T(V,E) =  O(|V|+|E|) 
    G2 = graph_AM.Graph(G.vertices,directed=True)
    for src in range(G.vertices):
        for dest in range(G.AM.shape[0]):
            if G.AM[src][dest] != -1:
                G2.insert_edge(dest,src)
    return G2
      
def reversed_edges(G):
    # T(V,E) =  O(|V|+|E|) 
    if type(G) == graph_AL.Graph:
       return reversed_edges_AL(G)
    elif type(G) == graph_AM.Graph:
        return reversed_edges_AM(G)
    print("Not AL or AM")

def is_isolated_AL(G,v):
    # T(V,E) =  O(|V|+|E|)
    if len(G.AL[v]) != 0:
        return False 
    for edges in G.AL:
        for edge in edges:
            if edge.dest == v:
                return False
    return True

def is_isolated_AM(G,v):
    # T(V,E) =  O(|V|) 
    if np.sum(G.AM[v]!=-1) != 0:
        return False
    if np.sum(G.AM[:,v]!=-1) != 0:
        return False
    return True
   
def is_isolated(G,v):
    # T(V,E) =  O(|V|) 
    if type(G) == graph_AL.Graph:
       return is_isolated_AL(G,v)
    elif type(G) == graph_AM.Graph:
        return is_isolated_AM(G,v)
    print("Not AL or AM")

def add_vertex_AL(G):
    return G.AL.append([])

def add_vertex_AM(G):
    NG = np.zeros((G.AM.shape[0]+1, G.AM.shape[0]+1),dtype=int)-1
    NG[:-1,:-1] = G.AM
    G.AM=NG
    return G.AM

def nearest_neighbor_AL(G,v):
    for edge in G.AL[v]:
        return [edge.dest] 
    return []

def nearest_neighbor_Am(G,v):
    for i in range(G.AM.shape[0]):
        if G.AM[v][i] != -1:
            return [i]
    return []

if __name__ == "__main__":

    plt.close("all")

    print('Question 1')
    G1 = graph_AL.Graph(6,directed=True) # Unweighted directed graph
    G1.insert_edge(0,1)
    G1.insert_edge(2,0)
    G1.insert_edge(2,5)
    G1.insert_edge(5,1)
    G1.insert_edge(4,1)
    G1.insert_edge(5,4)
    G1.insert_edge(2,3)
    G1.insert_edge(1,2)
    G1.display('G1')
    G1.draw('G1')
    
    for v in range(len(G1.AL)):
        print('Neighbors of',v,':',neighbors_AL(G1,v))
    
    print('Question 2')
    G2 = graph_AM.Graph(6,directed=True) # Unweighted directed graph
    G2.insert_edge(0,1)
    G2.insert_edge(2,0)
    G2.insert_edge(2,5)
    G2.insert_edge(5,1)
    G2.insert_edge(4,1)
    G2.insert_edge(5,4)
    G2.insert_edge(2,3)
    G2.insert_edge(1,2)
    G2.display('G2')
    G2.draw('G2')
    for v in range(G2.AM.shape[0]):
        print('Neighbors of',v,':',neighbors_AM(G2,v))
    
    print('Question 3')
    n_vert = len(G1.AL)
    print('Using Adjacency list representation')
    for v in range(n_vert):
        print('Neighbors of',v,':',neighbors(G1,v))
    print('Using Adjacency matrix representation')
    for v in range(n_vert):
        print('Neighbors of',v,':',neighbors(G2,v))
    
    print('Question 4')
    G1_r = reversed_edges_AL(G1)
    G1_r.display('G1_r')
    G1_r.draw('reversed_edges_AL(G1)')
    
    print('Question 5')
    G2_r = reversed_edges_AM(G2)
    G2_r.display('G1_r')
    G2_r.draw('reversed_edges_AM(G2)')
    
    print('Question 6')
    print('Using Adjacency list representation')
    G1_r = reversed_edges(G1)
    G1_r.display('G1_r')
    G1_r.draw('reversed_edges(G1)')
    print('Using Adjacency matrix representation')
    G2_r = reversed_edges(G2)
    G2_r.display('G1_r')
    G2_r.draw('reversed_edges(G2)')
    
    print('Question 7')
    G7 = graph_AL.Graph(7,directed=True) # Unweighted directed graph
    G7.insert_edge(2,0)
    G7.insert_edge(2,5)
    G7.insert_edge(5,1)
    G7.insert_edge(4,1)
    G7.insert_edge(5,4)
    G7.insert_edge(1,2)
    G7.display('G7')
    G7.draw('Graph for question 7')
    for v in range(len(G7.AL)):
        print('is_isolated_AL(G7,{}) = {}'.format(v,is_isolated_AL(G7,v)))
     
    print('Question 8')
    G8 = graph_AM.Graph(7,directed=True) # Unweighted directed graph
    G8.insert_edge(2,0)
    G8.insert_edge(2,5)
    G8.insert_edge(5,1)
    G8.insert_edge(4,1)
    G8.insert_edge(5,4)
    G8.insert_edge(1,2)
    G8.display('G8')
    G8.draw('Graph for question 8')
    for v in range(len(G8.AM)):
        print('is_isolated_AM(G8,{}) = {}'.format(v,is_isolated(G8,v)))
        
    print('Question 9')
    print('Using Adjacency list representation')
    for v in range(len(G7.AL)):
        print('is_isolated(G7,{}) = {}'.format(v,is_isolated(G7,v)))
    print('Using Adjacency matrix representation')
    for v in range(len(G8.AM)):
        print('is_isolated(G8,{}) = {}'.format(v,is_isolated(G8,v)))
        
    print('add AL')
    AddAL = add_vertex_AL(G1)
    AddAL.display('G1_r')
    AddAL.draw('add_vertex_AL(G1)')
        
    print('add AL')
    Add = add_vertex_AM(G2)
    Add.display('Add')
    Add.draw('add_vertex_AM(G2)')
     
'''
Expected Output
Question 1
G1 representation
directed: True, weighted: False
Adjacency list:
AL[0]=[(1,1)]
AL[1]=[(2,1)]
AL[2]=[(0,1), (5,1), (3,1)]
AL[3]=[]
AL[4]=[(1,1)]
AL[5]=[(1,1), (4,1)]
Neighbors of 0 : [1]
Neighbors of 1 : [2]
Neighbors of 2 : [0, 5, 3]
Neighbors of 3 : []
Neighbors of 4 : [1]
Neighbors of 5 : [1, 4]
Question 2
G2 representation
directed: True, weighted: False
Adjacency matrix:
[[-1  1 -1 -1 -1 -1]
 [-1 -1  1 -1 -1 -1]
 [ 1 -1 -1  1 -1  1]
 [-1 -1 -1 -1 -1 -1]
 [-1  1 -1 -1 -1 -1]
 [-1  1 -1 -1  1 -1]]
Neighbors of 0 : [1]
Neighbors of 1 : [2]
Neighbors of 2 : [0, 3, 5]
Neighbors of 3 : []
Neighbors of 4 : [1]
Neighbors of 5 : [1, 4]
Question 3
Using Adjacency list representation
Neighbors of 0 : [1]
Neighbors of 1 : [2]
Neighbors of 2 : [0, 5, 3]
Neighbors of 3 : []
Neighbors of 4 : [1]
Neighbors of 5 : [1, 4]
Using Adjacency matrix representation
Neighbors of 0 : [1]
Neighbors of 1 : [2]
Neighbors of 2 : [0, 3, 5]
Neighbors of 3 : []
Neighbors of 4 : [1]
Neighbors of 5 : [1, 4]
Question 4
G1_r representation
directed: True, weighted: False
Adjacency list:
AL[0]=[(2,1)]
AL[1]=[(0,1), (4,1), (5,1)]
AL[2]=[(1,1)]
AL[3]=[(2,1)]
AL[4]=[(5,1)]
AL[5]=[(2,1)]
Question 5
G1_r representation
directed: True, weighted: False
Adjacency matrix:
[[-1 -1  1 -1 -1 -1]
 [ 1 -1 -1 -1  1  1]
 [-1  1 -1 -1 -1 -1]
 [-1 -1  1 -1 -1 -1]
 [-1 -1 -1 -1 -1  1]
 [-1 -1  1 -1 -1 -1]]
Question 6
Using Adjacency list representation
G1_r representation
directed: True, weighted: False
Adjacency list:
AL[0]=[(2,1)]
AL[1]=[(0,1), (4,1), (5,1)]
AL[2]=[(1,1)]
AL[3]=[(2,1)]
AL[4]=[(5,1)]
AL[5]=[(2,1)]
Using Adjacency matrix representation
G1_r representation
directed: True, weighted: False
Adjacency matrix:
[[-1 -1  1 -1 -1 -1]
 [ 1 -1 -1 -1  1  1]
 [-1  1 -1 -1 -1 -1]
 [-1 -1  1 -1 -1 -1]
 [-1 -1 -1 -1 -1  1]
 [-1 -1  1 -1 -1 -1]]
Question 7
G7 representation
directed: True, weighted: False
Adjacency list:
AL[0]=[]
AL[1]=[(2,1)]
AL[2]=[(0,1), (5,1)]
AL[3]=[]
AL[4]=[(1,1)]
AL[5]=[(1,1), (4,1)]
AL[6]=[]
is_isolated_AL(G7,0) = False
is_isolated_AL(G7,1) = False
is_isolated_AL(G7,2) = False
is_isolated_AL(G7,3) = True
is_isolated_AL(G7,4) = False
is_isolated_AL(G7,5) = False
is_isolated_AL(G7,6) = True
Question 8
G8 representation
directed: True, weighted: False
Adjacency matrix:
[[-1 -1 -1 -1 -1 -1 -1]
 [-1 -1  1 -1 -1 -1 -1]
 [ 1 -1 -1 -1 -1  1 -1]
 [-1 -1 -1 -1 -1 -1 -1]
 [-1  1 -1 -1 -1 -1 -1]
 [-1  1 -1 -1  1 -1 -1]
 [-1 -1 -1 -1 -1 -1 -1]]
is_isolated_AM(G8,0) = False
is_isolated_AM(G8,1) = False
is_isolated_AM(G8,2) = False
is_isolated_AM(G8,3) = True
is_isolated_AM(G8,4) = False
is_isolated_AM(G8,5) = False
is_isolated_AM(G8,6) = True
Question 9
Using Adjacency list representation
is_isolated(G7,0) = False
is_isolated(G7,1) = False
is_isolated(G7,2) = False
is_isolated(G7,3) = True
is_isolated(G7,4) = False
is_isolated(G7,5) = False
is_isolated(G7,6) = True
Using Adjacency matrix representation
is_isolated(G8,0) = False
is_isolated(G8,1) = False
is_isolated(G8,2) = False
is_isolated(G8,3) = True
is_isolated(G8,4) = False
is_isolated(G8,5) = False
is_isolated(G8,6) = True
'''       

