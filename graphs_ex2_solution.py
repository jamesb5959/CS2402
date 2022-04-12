import numpy as np
import matplotlib.pyplot as plt
import graph_AL
import graph_AM

def neighbors_AL(G,v):
    # T(V,E) =  O(|V|) - A vertex can have at most |V|-1 neighbors
    return [edge.dest for edge in G.AL[v]]

def neighbors_AM(G,v):
    # T(V,E) =  O(|V|) - A row in an adjacency matrix has |V| elements
    return [i for i in range(len(G.AM[v])) if G.AM[v,i]!=-1]

def neighbors(G,v):
    # T(V,E) =  O(|V|) - Larger of running times of neighbors_AL(G,v) and neighbors_AM(G,v)
    if type(G) == graph_AL.Graph:
        return neighbors_AL(G,v)
    if type(G) == graph_AM.Graph:
        return neighbors_AM(G,v)
    print('Error, unexpected data type!')

def reversed_edges_AL(G):
    # T(V,E) =  O(|V|+|E|) - We need to traverse the whole list of lists. G.AL contains |V| list, and the combined length of
    # all lists in G.AL is |E|
    Gr = graph_AL.Graph(len(G.AL), weighted=G.weighted, directed = G.directed)
    for v in range(len(G.AL)):
        for edge in G.AL[v]:
            Gr.insert_edge(edge.dest, v, edge.weight)
    return Gr

def reversed_edges_AM(G):
    # T(V,E) =  O(|V|^2) - We build an array with |V| rows and |V| columns
    Gr = graph_AM.Graph(len(G.AM), weighted=G.weighted, directed = G.directed)
    #Gr.AM = G.AM.T
    for u in range(G.AM.shape[0]):
        for v in range(G.AM.shape[0]):
            Gr.AM[u,v] = G.AM[v,u]
    return Gr

def reversed_edges(G):
    # T(V,E) =  O(|V|^2) - Larger of running times of reversed_edges_AL(G) and reversed_edges_AM(G)
    if type(G) == graph_AL.Graph:
        return reversed_edges_AL(G)
    if type(G) == graph_AM.Graph:
        return reversed_edges_AM(G)
    print('Error, unexpected data type!')

def is_isolated_AL(G,v):
    # T(V,E) =  O(|V|+|E|) - We need to traverse the whole list of lists. G.AL contains |V| list, and the combined length of
    # all lists in G.AL is |E|
    if len(G.AL[v])>0:
        return False
    for u in range(len(G.AL)):
        #if v in [edge.dest for edge in G.AL[u]]:
        if v in neighbors_AL(G,u):
            return False
    return True

def is_isolated_AM(G,v):
    # T(V,E) =  O(|V|) - We need to travers one row and one column of G.AM; each of them has |V| elements
    return np.sum(G.AM[v]==-1)==len(G.AM) and np.sum(G.AM[:,v]==-1)==len(G.AM)

def is_isolated(G,v):
    # T(V,E) =  O(|V|+|E|) - Larger of running times of is_isolated_AL(G,v) and is_isolated_AM(G,v)
    if type(G) == graph_AL.Graph:
        return is_isolated_AL(G,v)
    if type(G) == graph_AM.Graph:
        return is_isolated_AM(G,v)
    print('Error, unexpected data type!')

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

