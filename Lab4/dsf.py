# Implementation of disjoint set forest (a.k.a. union/find data structure)
# Programmed by Olac Fuentes
# Last modified November 4, 2021
# Includes path compression and union by rank

from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt

class DSF:
    # Constructor
    def __init__(self, n_sets):
        # Creates forest with 'n_sets' root nodes
        self.parent = [-1 for i in range(n_sets)]

    def find(self,i):
        # Returns root of tree that i belongs to
        if self.parent[i]<0:
            return i
        root =  self.find(self.parent[i])
        self.parent[i] = root
        return root

    def union(self,i,j):
        # Joins i's tree and j's tree if they are different
        # Makes root of smaller tree point to root of larger tree
        # Returns 1 if a parent reference was changed, 0 otherwise
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.parent[root_i]<self.parent[root_j]:
                self.parent[root_i] += self.parent[root_j]
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] += self.parent[root_i]
                self.parent[root_i] = root_j
            return 1
        return 0

    def in_same_set(self,i,j):
        return self.find(i) == self.find(j)

    def set_list(self):
        # Returns a list of the sets encoded by the dsf
        set_dict = {i:set([i]) for i in range(len(self.parent)) if self.parent[i]<0}
        for i in range(len(self.parent)):
            if self.parent[i]>=0:
                set_dict[self.find(i)].add(i)
        return [set_dict[x] for x in set_dict]

    def draw(self,title=''):
        scale = 30
        figsize = [6.4, 2.4]
        if len(self.parent)>8:
            figsize[0] = 6.4*len(self.parent)/8
        fig, ax = plt.subplots(figsize=figsize)
        for i in range(len(self.parent)):
            if self.parent[i]<0:
                ax.plot([i*scale,i*scale],[0,scale],linewidth=1,color='k')
                ax.plot([i*scale-1,i*scale,i*scale+1],[scale-2,scale,scale-2],linewidth=1,color='k')
            else:
                x = np.linspace(i*scale,self.parent[i]*scale)
                x0 = np.linspace(i*scale,self.parent[i]*scale,num=5)
                diff = np.abs(self.parent[i]-i)
                if diff == 1:
                    y0 = [0,0,0,0,0]
                else:
                    y0 = [0,-6*diff,-8*diff,-6*diff,0]
                f = interp1d(x0, y0, kind='cubic')
                y = f(x)
                ax.plot(x,y,linewidth=1,color='k')
                ax.plot([x0[2]+2*np.sign(i-self.parent[i]),x0[2],x0[2]+2*np.sign(i-self.parent[i])],[y0[2]-1,y0[2],y0[2]+1],linewidth=1,color='k')
            ax.text(i*scale,0, str(i), size=20,ha="center", va="center",
             bbox=dict(facecolor='w',boxstyle="circle"))
        ax.axis('off')
        ax.set_aspect(1.0)
        if len(title)>0:
            fig.suptitle(title, fontsize=16)
        else:
            plt.tight_layout()
        plt.show()