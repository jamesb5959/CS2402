# Adjacency list representation of graphs
# Programmed by Olac Fuentes
# Last modified July 11, 2021

import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.interpolate import interp1d

class Edge:
    def __init__(self, dest, weight=1):
        self.dest = dest
        self.weight = weight

class Graph:
    # Constructor
    def __init__(self, n, weighted=False, directed = False):
        # T(V,E) = O(|V|) - We create |V| empty lists
        self.AL = [[] for i in range(n)]
        self.weighted = weighted
        self.directed = directed
        self.vertices = n

    def copy(self):
        # T(V,E) = O(|V|+|E|) - We traverse the whole graph
        # If the graph has less than |V| edges, we still perform |V| steps (the outer loop)
        # Otherwise, we will visit |E| edges
        g_copy = Graph(len(self.AL),self.weighted,self.directed)
        for i in range(len(self.AL)):
            for edge in self.AL[i]:
                 if self.directed or edge.dest>i:
                     g_copy.insert_edge(i,edge.dest,edge.weight)
        return g_copy

    def insert_edge(self,source,dest,weight=1):
        # T(V,E) = O(1) - We append an element to a list
        if source >= len(self.AL) or dest>=len(self.AL) or source <0 or dest<0:
            print('Error, vertex number out of range')
            return False
        elif weight!=1 and not self.weighted:
            print('Error, inserting weighted edge to unweighted graph')
            return False
        else:
            self.AL[source].append(Edge(dest,weight))
            if not self.directed:
                self.AL[dest].append(Edge(source,weight))
            return True

    def delete_edge_directed(self,source,dest):
        # T(V,E) = O(|V|) - We need to traverse the list of edges going out from source, which has length at most |V|-1
        for i,edge in enumerate(self.AL[source]):
            if edge.dest == dest:
                self.AL[source].pop(i)
                return True
        return False

    def delete_edge(self,source,dest):
        # T(V,E) = O(|V|) - We need to traverse the lists of edges going out from source and dest, which have length at most |V|-1
        if source >= len(self.AL) or dest>=len(self.AL) or source <0 or dest<0:
            print('Error, vertex number out of range')
        else:
            deleted = self.delete_edge_directed(source,dest)
            if not self.directed:
                deleted = self.delete_edge_directed(dest,source)
        if not deleted:
            print('Error, edge to delete not found')

    def display(self,name ='Graph'):
        # T(V,E) = O(|V|+|E|) - We traverse the whole graph
        # If the graph has less than |V| edges, we still perform |V| steps (the outer loop)
        # Otherwise, we will visit |E| edges
        print(name+' representation')
        print('directed: {}, weighted: {}'.format(self.directed,self.weighted))
        print('Adjacency list:')
        for i in range(len(self.AL)):
            p=''
            print('AL[{}]=['.format(i),end='')
            for edge in self.AL[i]:
                print(p+'({},{})'.format(edge.dest,edge.weight),end='')
                p=', '
            print(']')

    def draw(self,title=''):
        scale = 30
        figsize = [6.4, 3.5]
        if len(self.AL)>8:
            figsize[0] = 6.4*len(self.AL)/8
            scale = scale*len(self.AL)/8
        r = scale/5
        fig, ax = plt.subplots(figsize=figsize)
        for i in range(len(self.AL)):
            for edge in self.AL[i]:
                d,w = edge.dest, edge.weight
                if self.directed or d>=i:
                    x0 = np.linspace(i*scale,d*scale,num=5)
                    diff = np.abs(d-i)
                    if diff == 1:
                        y0 = [0,0,0,0,0]
                    else:
                        y0 = [0,-6*diff,-8*diff,-6*diff,0]
                    if  diff==0:
                        x = i*scale + r*np.sin(np.linspace(0,6.3))
                        y = r + r*np.cos(np.linspace(0,6.3))
                        y0 = [0,r,2*r,r,0]
                    else:
                        f = interp1d(x0, y0, kind='cubic')
                        x = np.linspace(i*scale,d*scale)
                        y = f(x)
                    s = np.sign(i-d-1/2)
                    ax.plot(x,s*y,linewidth=1,color='k')
                    if self.directed:
                        xd = [x0[2]+2*s,x0[2],x0[2]+2*s]
                        yd = [y0[2]-1,y0[2],y0[2]+1]
                        yd = [y*s for y in yd]
                        ax.plot(xd,yd,linewidth=1,color='k')
                    if self.weighted:
                        xd = [x0[2]+2*s,x0[2],x0[2]+2*s]
                        yd = [y0[2]-1,y0[2],y0[2]+1]
                        yd = [y*s for y in yd]
                        ax.text(xd[2]-s*3,yd[2]-3*s, str(w), size=10,ha="center", va="center")
                        #ax.text(xd[2]-s*2,yd[2]+3*s, str(w), size=12,ha="center", va="center")
            ax.plot([i*scale,i*scale],[0,0],linewidth=3,color='k')
            ax.text(i*scale,0, str(i), size=20,ha="center", va="center",
             bbox=dict(facecolor='w',boxstyle="circle"))
        ax.axis('off')
        ax.set_aspect(1.0)
        plt.tight_layout()
        fig.suptitle(title, fontsize=14)

if __name__ == "__main__":
    plt.close("all")
    g = Graph(5)
    g.insert_edge(0,1)
    g.insert_edge(0,2)
    g.insert_edge(1,2)
    g.insert_edge(2,3)
    g.insert_edge(3,4)
    g.insert_edge(4,1)
    g.display()
    g.draw()
    g.delete_edge(1,2)
    g.display()
    g.draw()


    g = Graph(5,directed = True)
    g.insert_edge(0,1)
    g.insert_edge(0,2)
    g.insert_edge(1,2)
    g.insert_edge(2,3)
    g.insert_edge(3,4)
    g.insert_edge(4,1)
    g.display()
    g.draw()
    g.delete_edge(1,2)
    g.display()
    g.draw()

    g = Graph(5,weighted=True)
    g.insert_edge(0,1,4)
    g.insert_edge(0,2,3)
    g.insert_edge(1,2,2)
    g.insert_edge(2,3,1)
    g.insert_edge(3,4,5)
    g.insert_edge(4,1,4)
    g.display()
    g.draw()
    g.delete_edge(1,2)
    g.display()
    g.draw()

    g = Graph(5,weighted=True,directed = True)
    g.insert_edge(0,1,4)
    g.insert_edge(0,2,3)
    g.insert_edge(1,2,2)
    g.insert_edge(2,3,1)
    g.insert_edge(3,4,5)
    g.insert_edge(4,1,4)
    g.display()
    g.draw()
    g.delete_edge(1,2)
    g.display()
    g.draw()



#for v in range(len(G.AL)):
        #for edge in G.AL[v]:
