# Adjacency matrix representation of graphs
# Programmed by Olac Fuentes
# Last modified July 13, 2021

import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.interpolate import interp1d

class Graph:
    def __init__(self, n, weighted=False, directed = False):
        # T(V,E) = O(|V|^2) - Since we must create and initialize a matrix with
        # |V| rows and |V| columns
        self.AM = np.zeros((n,n),dtype=int)-1
        self.weighted = weighted
        self.directed = directed
        self.vertices = n


    def insert_edge(self,source,dest,weight=1):
        # T(V,E) = O(1) - We can access the appropriate position in AM directly
        if source >= self.AM.shape[0] or dest>=self.AM.shape[1] or source <0 or dest<0:
            print('Error, vertex number out of range')
            return False
        elif weight!=1 and not self.weighted:
            print('Error, inserting weighted edge to unweighted graph')
            return False
        else:
            self.AM[source,dest]=weight
            if not self.directed:
                self.AM[dest,source]=weight
            return True

    def delete_edge(self,source,dest):
        # T(V,E) = O(1) - We can access the appropriate position in AM directly
        self.AM[source,dest]=-1
        if not self.directed:
            self.AM[dest,source]=-1

    def display(self,name ='Graph'):
        # T(V,E) = O(|V|^2) - Since we must traverse the adjacency matrix
        # which has |V| rows and |V| columns
        print(name+' representation')
        print('directed: {}, weighted: {}'.format(self.directed,self.weighted))
        print('Adjacency matrix:')
        print(self.AM)

    def draw(self,title=''):
        # T(V,E) = O(|V|^2) - Since we must traverse the adjacency matrix
        # which has |V| rows and |V| columns
        scale = 30
        figsize = [6.4, 3.5]
        if self.AM.shape[0]>8:
            figsize[0] = 6.4*self.AM.shape[0]/8
            scale = scale*len(self.AM)/8
        fig, ax = plt.subplots(figsize=figsize)
        r = scale/5

        for i in range(self.AM.shape[0]):
            for d in range(self.AM.shape[1]):
                w = self.AM[i,d]
                if w!=-1:
                    if self.directed or d>i:
                        x = np.linspace(i*scale,d*scale)
                        x0 = np.linspace(i*scale,d*scale,num=5)
                        diff = np.abs(d-i)
                        if diff == 1:
                            y0 = [0,0,0,0,0]
                        else:
                            y0 = [0,-6*diff,-8*diff,-6*diff,0]
                        f = interp1d(x0, y0, kind='cubic')
                        y = f(x)
                        s = np.sign(i-d)
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
                            ax.text(xd[2]-s*3,yd[2]-4*s, str(w), size=10,ha="center", va="center")
                            #ax.text(xd[2]-s*2,yd[2]+3*s, str(w), size=12,ha="center", va="center")

                ax.plot([i*scale,i*scale],[0,0],linewidth=1,color='k')
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

#for e in range(G.AM.shape[0]):
#        if G.AM[u,e]>0 and G.AM[e,v]>0 and G.AM[e,x]>0:


#for u in range(G.AM.shape[0]):
#       for v in range(G.AM.shape[0]):