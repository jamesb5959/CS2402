# Code to implement B-trees
# Programmed by Olac Fuentes
# Last modified September 23, 2021

import matplotlib.pyplot as plt
import numpy as np

class BTree:
    # Constructor
    def __init__(self,  max_items = 5, d = [],c = []):
        if max_items%2 ==0: # Make sure max_items is odd
            max_items +=1
        if max_items <3:    # Make sure max_items is  at least 3
            max_items=3

        self.data = d
        self.child = c
        self.max_items = max_items

    def find_subtree(self, k):
        # Determines value of c, such that if i is in the BTree, it must be in subtree self.child[c]
        for c in range(len(self.data)):
            if self.data[c]>k:
                return c
        return len(self.data)

    def is_full(self):
        return len(self.data) >= self.max_items

    def insert(self, i, parent=None):
        if self.is_full():
            m, right_child = self.split()
            if parent==None: # Spliting the root
                left_child = BTree(self.max_items,self.data,self.child)
                self.data = [m]
                self.child = [left_child, right_child]
                if i<m:
                    left_child.insert(i,self)
                else:
                    right_child.insert(i,self)
            else: # Splitting non-root node
                k = parent.find_subtree(i)
                parent.data = parent.data[:k]+[m]+parent.data[k:]
                parent.child = parent.child[:k+1]+[right_child]+parent.child[k+1:]
                if i<m:
                    self.insert(i,parent)
                else:
                    right_child.insert(i,parent)
        else: # Node is not full; no need to split it
            k = self.find_subtree(i)
            if len(self.child)==0: # If node is a leaf, insert new item here
                self.data = self.data[:k]+[i]+self.data[k:]
            else:
                self.child[k].insert(i,self) # Insert in appropriate subtree

    def split(self):
        mid = self.max_items // 2
        m = self.data[mid]
        right_side = BTree(self.max_items,self.data[mid + 1:],self.child[mid + 1:])
        self.data = self.data[:mid]
        self.child = self.child[:mid+1]
        return m, right_side

    def _leaves(self):
        if len(self.child)==0:
            return [self.data]
        s = []
        for c in self.child:
            s = s + c._leaves()
        return s

    def _set_x(self, dx):
        if len(self.child)>0:
            for c in self.child:
                c._set_x(dx)
            d = (dx[self.child[0].data[0]] + dx[self.child[-1].data[0]] + 10 * len(self.child[-1].data)) / 2
            dx[self.data[0]] = d - 10 * len(self.data) / 2

    def draw_(self, dx, y, y_inc, fs, ax):
        # Function to display b-tree to the screen
        # It works fine for trees with up to about 70 data items
        xs = dx[self.data[0]]
        if len(self.child)==0:
            for itm in self.data:
                ax.plot([xs, xs + 10, xs + 10, xs, xs], [y, y, y - 10, y - 10, y], linewidth=1, color='k')
                ax.text(xs + 5, y - 5, str(itm), ha="center", va="center", fontsize=fs)
                xs += 10
        else:
            for i,d in enumerate(self.data):
                xc = dx[self.child[i].data[0]] + 5 * len(self.child[i].data)
                ax.plot([xs, xs + 10, xs + 10, xs, xs], [y, y, y - 10, y - 10, y], linewidth=1, color='k')
                ax.text(xs + 5, y - 5, str(d), ha="center", va="center", fontsize=fs)
                ax.plot([xs, xc], [y - 10, y - y_inc], linewidth=1, color='k')
                self.child[i].draw_(dx, y - y_inc, y_inc, fs, ax)
                xs += 10
            xc = dx[self.child[-1].data[0]] + 5 * len(self.child[-1].data)
            ax.plot([xs, xc], [y - 10, y - y_inc], linewidth=1, color='k')
            self.child[-1].draw_(dx, y - y_inc, y_inc, fs, ax)

    def draw(self,title=''):
        # Find x-coordinates of leaves
        ll = self._leaves()
        dx = {}
        d = 0
        for l in ll:
            dx[l[0]] = d
            d += 10 * (len(l) + 1)
            # Find x-coordinates of internal nodes
        self._set_x(dx)
        # plt.close('all')
        fig, ax = plt.subplots(figsize=(8,3))
        self.draw_(dx, 0, 30, 9, ax)
        ax.set_aspect(1.0)
        ax.axis('off')
        fig.suptitle(title, fontsize=14)
        plt.tight_layout()
        plt.show()

    def print_tree(self,space=''):
        print(space,self.data)
        for c in self.child:
            c.print_tree(space+'  ')

if __name__ == "__main__":
    plt.close('all')
    A =[8, 11, 6, 7, 16, 2,15, 1, 9, 4, 14,  13, 5,3,10,12,17]
    np.random.seed(0)
    A =list(np.random.permutation(45)*2)

    A.append(47)

    T = BTree(4)

    for a in A:
        T.insert(a)

    T.print_tree()


    T.draw()

    #if T.is_empty:
    #    return False
    #c =[t.key for t in [T.left,T.right] if not t.is_empty]
    #return k in c