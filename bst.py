# Code to implement basic binary search tree operations
# Programmed by Olac Fuentes
# Last modified September 13, 2021

import matplotlib.pyplot as plt
import numpy as np

class BST:

    def __init__(self, key=None, left=None, right=None):
        # Constructor 
        if (key==None): # if key is None, it will create an empty tree
            self.is_empty = True
        else:
            self.is_empty = False
            self.key=key
            if left==None:
                self.left=BST()
            else:
                self.left=left
            if right==None:
                self.right=BST()
            else:
                self.right=right

    def insert(self,newkey):
        if self.is_empty: # If tree is empty - create a one-node tree containing newkey
            self.is_empty = False
            self.key=newkey
            self.left=BST()
            self.right=BST()
        else:
            if self.key>newkey:  # Insert newkey in left subtree
                self.left.insert(newkey)
            else:                # Insert newkey in right subtree
                self.right.insert(newkey)

    def in_order(self):
        # In-order traversal. Prints keys in tree in ascending order
        if not self.is_empty:
            self.left.in_order()
            print(self.key,end=' ')
            self.right.in_order()


    def find(self,key,parent=None,return_parent=False):
        # Returns address of node where key is. 
        # If return_parent is True, it also returns the parent of the node where key is
        # Returning the parent makes deletions simpler
        if self.is_empty:
            if return_parent:
                return parent, None
            return None
        if self.key == key:
            if return_parent:
                return parent, self
            return self
        if self.key>key:
            return self.left.find(key,self,return_parent)
        return self.right.find(key,self,return_parent)

    def delete(self,key):
        parent, node = self.find(key,None,True)
        if node==None:
            print('key to delete was not found in tree!')
            return
        children = [t for t in [node.left,node.right] if not t.is_empty]
        if len(children)==0: # Case 1, just delete the leaf
            if parent == None: # If the leaf to delete is also the root, the tree becomes empty
                self.is_empty = True
            elif parent.left == node:  parent.left = BST()
            else:  parent.right = BST()
        elif len(children)==1: # Case 2, make parent point to node's only child
            if parent == None: # If the node to delete the root, it's only child becomes the new root
                t = children[0]
                self.key = t.key
                self.left = t.left
                self.right = t.right
            elif parent.left == node:  parent.left = children[0]
            else:  parent.right = children[0]
        else: # Case 3
            s = node.right
            while not s.left.is_empty: # Find smallest key in node's right subtree (key's successor)
                s = s.left
            temp = s.key
            node.delete(s.key)  # Delete the node containing the key's successor
            node.key = temp     # Copy the succesor to the current node

    ######## Functions to draw BSTs to the screen  
    def draw(self,title=''):
        if self.is_empty:
            print('Empty tree, nothing to draw')
        else:
            dx ={}
            self.set_xy(dx)
            fig, ax = plt.subplots()
            self.draw_(ax, dx)
            ax.axis('off')
            fig.suptitle(title, fontsize=14)
            plt.show()

    def draw_(self, ax, dx):
        # Auxiliary function used by the drawing function
        if not self.is_empty:
            px, py = dx[self]
            for child in [self.left, self.right]:
                if not child.is_empty:
                    cx,cy = dx[child]
                    ax.plot([px,cx],[py,cy],linewidth=1,color='k')
                    child.draw_(ax,dx)
            ax.text(px,py, str(self.key), size=12,ha="center", va="center",bbox=dict(facecolor='w',boxstyle="circle"))

    def set_xy(self,dx,x=0,y=0):
        # Auxiliary function used by the drawing function, is find the image coordinates to draw the tree's nodes
        if not self.is_empty:
            next_x = self.left.set_xy(dx,x,y-1)
            dx[self] = (next_x,y)
            x = self.right.set_xy(dx,next_x+1,y-1)
        return x

    def print_tree(self,space=''):
        # Prints tree with structure, rotated 90 degrees
        # root is at leftmost position
        # maximum key is on the first line
        # miniimum key is on the last line
        if not self.is_empty:
            self.right.print_tree(space+'   ')
            print(space,self.key)
            self.left.print_tree(space+'   ')


   #if t.is_empty:
    #  return t

   #if d == 0:
    #  return bst.BST(key=t.key)
   
   #left = copy_bst_up_to_depth_d(t.left, d-1)
   #right = copy_bst_up_to_depth_d(t.right, d-1)
   #return bst.BST(t.key, left, right)



