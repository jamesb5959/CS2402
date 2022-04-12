import matplotlib.pyplot as plt
import numpy as np
import bst

def build_bst(L):
  T = bst.BST()
  for a in L:
    T.insert(a)
  return T

def reverse_pairs(word_list):
  result=[]
  setWord=set(word_list)
  setReverseL=set()
  for word in setWord:
    setReverseL.add(word[::-1])
  for reverseWord in setReverseL:
    if reverseWord in setWord:
      result.append(reverseWord)
  return sorted(result)

def bst_to_dict(T,D={}):
    if not T.is_empty:
      bst_to_dict(T.right,D)  
      D[T.key]=T
      bst_to_dict(T.left,D)
    return D

if __name__ == "__main__":
    plt.close('all')

    word_list = []
    with open('most_common_words.txt') as f:
        for line in f:
            word_list.append(line[:-1])

    print('Reverse_pairs')
    print(reverse_pairs(word_list))

    np.random.seed(0)
    L = np.random.permutation(12)
    T = build_bst(L)
    T.draw()

    D = bst_to_dict(T)
    for item in L:
        #D[item].draw(str(item)) # Uncomment to see subtrees drawn as trees
        print('Inorder traversal of subtree that has',item,'as root:' )
        D[item].in_order()
        print()

'''
Reverse_pairs
['', 'I', 'a', 'ah', 'civic', 'dad', 'dam', 'drawer', 'edit', 'evil', 'eye', 'flow', 'ha', 'huh', 'level', 'live', 'loop', 'mad', 'mom', 'net', 'no', 'noon', 'on', 'part', 'pat', 'pit', 'pool', 'pop', 'pot', 'radar', 'raw', 'refer', 'reward', 'tap', 'ten', 'tide', 'tip', 'top', 'trap', 'war', 'wolf', 'wow']
Inorder traversal of subtree that has 6 as root:
0 1 2 3 4 5 6 7 8 9 10 11
Inorder traversal of subtree that has 11 as root:
7 8 9 10 11
Inorder traversal of subtree that has 4 as root:
0 1 2 3 4 5
Inorder traversal of subtree that has 10 as root:
7 8 9 10
Inorder traversal of subtree that has 2 as root:
0 1 2 3
Inorder traversal of subtree that has 8 as root:
7 8 9
Inorder traversal of subtree that has 1 as root:
0 1
Inorder traversal of subtree that has 7 as root:
7
Inorder traversal of subtree that has 9 as root:
9
Inorder traversal of subtree that has 3 as root:
3
Inorder traversal of subtree that has 0 as root:
0
Inorder traversal of subtree that has 5 as root:
5

runfile('C:/Users/OFuentes/OneDrive - University of Texas at El Paso/CS2302/Part 3/exercises/exercise_sets_dictionaries.py', wdir='C:/Users/OFuentes/OneDrive - University of Texas at El Paso/CS2302/Part 3/exercises', current_namespace=True)
Reloaded modules: bst
['', 'I', 'a', 'ah', 'civic', 'dad', 'dam', 'drawer', 'edit', 'evil', 'eye', 'flow', 'ha', 'huh', 'level', 'live', 'loop', 'mad', 'mom', 'net', 'no', 'noon', 'on', 'part', 'pat', 'pit', 'pool', 'pop', 'pot', 'radar', 'raw', 'refer', 'reward', 'tap', 'ten', 'tide', 'tip', 'top', 'trap', 'war', 'wolf', 'wow']
Inorder traversal of subtree that has 6 as root:
0 1 2 3 4 5 6 7 8 9 10 11
Inorder traversal of subtree that has 11 as root:
7 8 9 10 11
Inorder traversal of subtree that has 4 as root:
0 1 2 3 4 5
Inorder traversal of subtree that has 10 as root:
7 8 9 10
Inorder traversal of subtree that has 2 as root:
0 1 2 3
Inorder traversal of subtree that has 8 as root:
7 8 9
Inorder traversal of subtree that has 1 as root:
0 1
Inorder traversal of subtree that has 7 as root:
7
Inorder traversal of subtree that has 9 as root:
9
Inorder traversal of subtree that has 3 as root:
3
Inorder traversal of subtree that has 0 as root:
0
Inorder traversal of subtree that has 5 as root:
5
'''