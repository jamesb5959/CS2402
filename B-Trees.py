import numpy as np
import matplotlib.pyplot as plt
import math

class BTree(object):
    # Constructor
    def __init__(self,item,child=[],isLeaf=True,max_items=5):  
        self.item = item
        self.child = child 
        self.isLeaf = isLeaf
        if max_items <3: #max_items must be odd and greater or equal to 3
            max_items = 3
        if max_items%2 == 0: #max_items must be odd and greater or equal to 3
            max_items +=1
        self.max_items = max_items

def FindChild(T,k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree    
    for i in range(len(T.item)):
        if k < T.item[i]:
            return i
    return len(T.item)
             
def InsertInternal(T,i):
    # T cannot be Full
    if T.isLeaf:
        InsertLeaf(T,i)
    else:
        k = FindChild(T,i)   
        if IsFull(T.child[k]):
            m, l, r = Split(T.child[k])
            T.item.insert(k,m) 
            T.child[k] = l
            T.child.insert(k+1,r) 
            k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
            
def Split(T):
    #print('Splitting')
    #PrintNode(T)
    mid = T.max_items//2
    if T.isLeaf:
        leftChild = BTree(T.item[:mid]) 
        rightChild = BTree(T.item[mid+1:]) 
    else:
        leftChild = BTree(T.item[:mid],T.child[:mid+1],T.isLeaf) 
        rightChild = BTree(T.item[mid+1:],T.child[mid+1:],T.isLeaf) 
    return T.item[mid], leftChild,  rightChild   
      
def InsertLeaf(T,i):
    T.item.append(i)  
    T.item.sort()

def IsFull(T):
    return len(T.item) >= T.max_items

def Leaves(T):
    # Returns the leaves in a b-tree
    if T.isLeaf:
        return [T.item]
    s = []
    for c in T.child:
        s = s + Leaves(c)
    return s

def Set_x(T,Dx):
    # Finds x-coordinate to display each node in the tree
    if T.isLeaf:
        return 
    else:
        for c in T.child:
            Set_x(c,Dx)
        d = (Dx[T.child[0].item[0]] + Dx[T.child[-1].item[0]] + 10*len(T.child[-1].item))/2
        Dx[T.item[0]] = d - 10*len(T.item)/2
        
def Insert(T,i):
    if not IsFull(T):
        InsertInternal(T,i)
    else:
        m, l, r = Split(T)
        T.item =[m]
        T.child = [l,r]
        T.isLeaf = False
        k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
     
def Height(T):
    if T.isLeaf:
        return 0
    return 1 + Height(T.child[0])    
    
def Print(T):
    # Prints items in tree in ascending order
    if T.isLeaf:
        for t in T.item:
            print(t,end=' ')
    else:
        for i in range(len(T.item)):
            Print(T.child[i])
            print(T.item[i],end=' ')
        Print(T.child[len(T.item)])    
         
def PrintD(T,space):
    # Prints items and structure of B-tree
    if T.isLeaf:
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
    else:
        PrintD(T.child[len(T.item)],space+'   ')  
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
            PrintD(T.child[i],space+'   ')
            
def DrawBtree_(T, Dx, y, y_inc, fs, ax):
    # Function to display b-tree to the screen 
    # It works fine for trees with up to about 70 items
    xs = Dx[T.item[0]]
    if T.isLeaf:
        for itm in T.item:
            ax.plot([xs,xs+10,xs+10,xs,xs],[y,y,y-10,y-10,y],linewidth=1,color='k')
            ax.text(xs+5,y-5, str(itm), ha="center", va="center",fontsize=fs)
            xs +=10
    else:
        for i in range(len(T.item)):
            xc = Dx[T.child[i].item[0]] + 5*len(T.child[i].item)
            ax.plot([xs,xs+10,xs+10,xs,xs],[y,y,y-10,y-10,y],linewidth=1,color='k')
            ax.text(xs+5,y-5, str(T.item[i]), ha="center", va="center",fontsize=fs)
            ax.plot([xs,xc],[y-10,y-y_inc],linewidth=1,color='k')
            DrawBtree_(T.child[i], Dx, y-y_inc, y_inc, fs, ax)
            xs +=10
        xc = Dx[T.child[-1].item[0]] + 5*len(T.child[-1].item)
        ax.plot([xs,xc],[y-10,y-y_inc],linewidth=1,color='k')
        DrawBtree_(T.child[-1], Dx, y-y_inc, y_inc, fs, ax)
    
def DrawBtree(T):
    #Find x-coordinates of leaves    
    LL = Leaves(T)
    Dx ={}
    d =0
    for L in LL:
        Dx[L[0]]=d 
        d += 10*(len(L)+1)  
    #Find x-coordinates of internal nodes
    Set_x(T,Dx)    
    #plt.close('all')
    fig, ax = plt.subplots()
    DrawBtree_(T, Dx, 0, 30, 10, ax)
    ax.set_aspect(1.0)
    ax.axis('off') 
    plt.show()
    
def SmallestAtDepthD(T,d):
    if T.isLeaf and d != 0:
      return math.inf
    elif d == 0:
      return T.item[0]
    else:
      return SmallestAtDepthD(T.child[0],d-1)

def LargestAtDepthD(T,d):
    if T.isLeaf and d != 0:
      return math.inf
    elif d == 0:
      return T.item[-1]
    else:
      return LargestAtDepthD(T.child[-1],d-1)
  
def Smallest_Range(T):
    if T.isLeaf:
        return T.item[-1] - T.item[0]
    return Smallest_Range(T.child[0])
  
def Diff(T,d):
    s = 0
    if T.isLeaf or d == 0:
        s += T.item[-1] - T.item[0]
        return s
    for c in T.child:
        s += Diff(c,d-1)
    return s

def Sum_LeftMost(T):
    s = T.item[0]
    if not T.isLeaf:
        for c in T.child:
            return s + Sum_LeftMost(c)
    return s

def FullNodesD(T,d):
    amt = 0
    if d == 0 and IsFull(T):
        amt += 1
    for c in T.child:
        amt += FullNodesD(c,d-1)
    return amt

def SameNode(T,k):
    n = []
    if k in T.item:
        n = T.item
    else:
        for c in T.child:
            n += SameNode(c,k)
    return n

def Predecessor(T,k):
    if T.isLeaf:
        for i in range(len(T.item)-1,-1,-1):
            if k>T.item[i]:
                return T.item[i]
        return -math.inf
    for i in range(len(T.item)):
        if k <= T.item[i]:
            ch = i
            break
    if k > T.item[-1]:
        ch = len(T.item)
    p =  Predecessor(T.child[ch],k)
    if p == -math.inf:
        if ch>0:
            return T.item[ch-1]
    return p


if __name__ == "__main__":        
    #T = BTree([])  
    #P = np.random.permutation(40)
    L=[19,15,1,2,4,25,18,13,9,20,24,6,3,23,16,22,11,7,17,14,8,5,21,10,12,26,27,28]
    #for i in P:
    #    Insert(T,i)
        
    #print('Keys in the tree: ')
    #Print(T) 
    #print()
    
    #print('Tree structure')
    #PrintD(T,'') 
    
    T = BTree([])  
    for i in L:
        Insert(T,i)
        
    print('Keys in the tree: ')
    Print(T) 
    print()
    
    print('Tree structure')
    PrintD(T,'') 
    
    print(Diff(T,0))
    print(Diff(T,1))
    print(Diff(T,2))
    print(Diff(T,3))
    print()
    print(Sum_LeftMost(T))
    print(Sum_LeftMost(T.child[1]))
    print()
    print(Smallest_Range(T))
    print()
    print(LargestAtDepthD(T,2))
    print()
    print(FullNodesD(T,2))
    print()
    print(SameNode(T,6))
    print()
    print('Predecessor: ')
    print(Predecessor(T,15))
    #if T.is_empty:
    #    return False
    #c =[t.key for t in [T.left,T.right] if not t.is_empty]
    #return k in c