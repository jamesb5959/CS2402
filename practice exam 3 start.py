import min_heap
import matplotlib.pyplot as plt
import numpy as np

def iou(L1,L2):
    # T(n) = O(n)
    set1 = set(L1)
    set2 = set(L2)
    setUnion = set1.union(set2)
    setIntersection = set1.intersection(set2)
    return len(setIntersection)/len(setUnion)

def sequence_locations(S,m):
    # T(n) = O(n)
    D={}
    for i in range(len(S)-m+1):
        subString=S[i:i+m]
        if subString not in D.keys():
            D[subString]=[i]
        else:
            D[subString]+=[i]
    return D

def change_key(H,k,m):
    # T(n) = O(log n)
    if len(H.heap) == 0 or k > len(H.heap) or k < 0 :
        return 
    if len(H.heap) == 1:
        H.heap[k] = m
        return 
    if H.heap[k].key >= m:
        H.heap[k].key = m
        H.bubble_up(k)
    elif H.heap[k].key < m:
        H.heap[k].key = m
        H.percolate_down(k)

if __name__ == "__main__":

    plt.close('all')
   
    print('Question 1')

    for i in range(2):
        np.random.seed(i+1)
        n1 = np.random.randint(4,10)
        n2 = np.random.randint(4,10)
        L1 = np.random.permutation(10)[:n1]
        L2 = np.random.permutation(10)[:n2]
        L1.sort()
        L2.sort()
        print('L1=',L1)
        print('L2=',L2)
        print('IoU=',iou(L1,L2))

    print('Question 2')
    
    S = 'ACCAAGGGTTTTGTAGGTGTATACATACCAGGGCAATCGGCAACACGTCTGGTGGAGGTGTGCATAGAACTGCAGTGAGTGTTCGATGTGTGTATTGATAA'
    print(S)
    for m in range(1,7):
        np.random.seed(i+1)
        print('Sequence length =',m)
        D = sequence_locations(S,m)
        for i in [0,1,6,9]:
            s = S[i:i+m]
            print('Sequence',s,'appears in locations',D[s])

    print('Question 3')
    L1 = [11, 13, 19,  9,  2,  6, 14, 21,  8,  7, 15, 10,  4,  3, 1]
    H =  min_heap.min_heap()
    for i in L1:
        H.insert(i)
    title = 'Original heap'    
    H.draw(title, indices=True)
    print(title,[h.key for h in H.heap])
    
    for p in [[1,19],[6,0],[10,2],[2,10]]:
        change_key(H,p[0],p[1])
        title= 'result of change_key(H,{},{})'.format(p[0],p[1])
        H.draw(title, indices=True)
        print(title,[h.key for h in H.heap])
       
'''
 Question 1
L1= [0 1 2 3 4 5 6 7 9]
L2= [0 1 3 5 7 8 9]
IoU= 0.6
L1= [1 4 5 9]
L2= [0 1 2 3 4 6 7 8 9]
IoU= 0.3
Question 2
ACCAAGGGTTTTGTAGGTGTATACATACCAGGGCAATCGGCAACACGTCTGGTGGAGGTGTGCATAGAACTGCAGTGAGTGTTCGATGTGTGTATTGATAA
Sequence length = 1
Sequence A appears in locations [0, 3, 4, 14, 20, 22, 24, 26, 29, 34, 35, 41, 42, 44, 55, 63, 65, 67, 68, 73, 77, 85, 93, 97, 99, 100]
Sequence C appears in locations [1, 2, 23, 27, 28, 33, 37, 40, 43, 45, 48, 62, 69, 72, 83]
Sequence G appears in locations [5, 6, 7, 12, 15, 16, 18, 30, 31, 32, 38, 39, 46, 50, 51, 53, 54, 56, 57, 59, 61, 66, 71, 74, 76, 78, 80, 84, 87, 89, 91, 96]
Sequence T appears in locations [8, 9, 10, 11, 13, 17, 19, 21, 25, 36, 47, 49, 52, 58, 60, 64, 70, 75, 79, 81, 82, 86, 88, 90, 92, 94, 95, 98]
Sequence length = 2
Sequence AC appears in locations [0, 22, 26, 42, 44, 68]
Sequence CC appears in locations [1, 27]
Sequence GG appears in locations [5, 6, 15, 30, 31, 38, 50, 53, 56]
Sequence TT appears in locations [8, 9, 10, 81, 94]
Sequence length = 3
Sequence ACC appears in locations [0, 26]
Sequence CCA appears in locations [1, 27]
Sequence GGT appears in locations [6, 15, 50, 56]
Sequence TTT appears in locations [8, 9]
Sequence length = 4
Sequence ACCA appears in locations [0, 26]
Sequence CCAA appears in locations [1]
Sequence GGTT appears in locations [6]
Sequence TTTG appears in locations [9]
Sequence length = 5
Sequence ACCAA appears in locations [0]
Sequence CCAAG appears in locations [1]
Sequence GGTTT appears in locations [6]
Sequence TTTGT appears in locations [9]
Question 3
Original heap [1, 7, 2, 9, 8, 6, 3, 21, 13, 11, 15, 19, 10, 14, 4]
result of change_key(H,1,19) [1, 8, 2, 9, 11, 6, 3, 21, 13, 19, 15, 19, 10, 14, 4]
result of change_key(H,6,0) [0, 8, 1, 9, 11, 6, 2, 21, 13, 19, 15, 19, 10, 14, 4]
result of change_key(H,10,2) [0, 2, 1, 9, 8, 6, 2, 21, 13, 19, 11, 19, 10, 14, 4]
result of change_key(H,2,10) [0, 2, 2, 9, 8, 6, 4, 21, 13, 19, 11, 19, 10, 14, 10]   
'''


