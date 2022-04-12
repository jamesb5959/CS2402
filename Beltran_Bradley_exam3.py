import matplotlib.pyplot as plt
import numpy as np
import min_heap

def read_words():
    word_list = []
    with open('most_common_words.txt') as f:
        for line in f:
            w = line[:-1]
            if len(w)>=3:
                word_list.append(line[:-1])
    return word_list

def build_heap(L):
    H = min_heap.min_heap()
    for i in L:
        H.insert(i)
    return H

def common_chars(w1,w2):
    #T(n) = O(n) because we look through the words with a loop
    L=[]
    for i in w1:
        if i in w2:
            L.append(i)
    return set(L)

def last_occurrence(S,m):
     #T(n) = O(n) because we use a for loop to go trough the whole string
    D={}
    for i in range(len(S)-m+1):
        subString=S[i:i+m]
        D[subString]=i
    return D

def key_list(H):
     #T(n) = O(n) because we use a for loop to go trough the whole heap
    L=[]
    for i in range(len(H.heap)):
        L.append(H.heap[i].key)
    return L

def appears_in_1(L1,L2):
     #T(n) = O(n) because we use a for loop to go through both list
    temp = L1+L2
    set1= set(temp)
    L=[]
    for i in L1:
        if i not in L2: 
            L.append(i)
    for i in L2:
        if i not in L1: 
            L.append(i)
    return set(L)

def first_3_letters(W):
    #T(n) = O(n) we use a for loop to go through all the words
    D ={}
    for i in W:
        subString = i[0:3]
        if subString in D:
            D[subString]+=[i]
        else:
            D[subString]=[i]
    return D


def extract_from_2_heaps(H1,H2,k):
    #T(n) = O(n log n) because we go and get the smallest value from each heap
    L = []
    for i in range(len(H1.heap)):
        if H1.heap[i].key<k:
            L.append(H1.heap[i].key)
    for i in range(len(H2.heap)):
        if H2.heap[i].key<k:
            L.append(H2.heap[i].key)
    return sorted(L)

if __name__ == "__main__":

    plt.close('all')

    print('Question 1')
    w1 = 'data'
    w2 = 'structures'
    w3 = 'utep'
    w4 = 'miners'

    for wa in [w1,w2,w3,w4]:
        for wb in [w1,w2,w3,w4]:
            print('common_chars({},{})'.format(wa,wb),end=': ')
            print(common_chars(wa,wb))

    
    print('Question 2')
    S = 'DATA'
    print('S =',S)
    for m in range(1,4):
        print('Sequence length =',m)
        D = last_occurrence(S,m)
        for i in range(len(S)-m):
            s = S[i:i+m]
            print('The last occurrence of',s,'is in location',D[s])

    S = 'ACCAAGGGTTTTGTAGGTGTATACATACCAGGGCAATCGGCAACACGTCTGGTGGAGGTGTGCATAGAACTGCAGTGAGTGTTCGATGTGTGTATTGATAA'
    print('S =',S)
    for m in range(1,6):
        print('Sequence length =',m)
        D = last_occurrence(S,m)
        for i in [0,1,6,9]:
            s = S[i:i+m]
            print('The last occurrence of',s,'is in location',D[s])
    
    
    print('Question 3')
    np.random.seed(0)
    for i in range(3):
        H3 = build_heap(np.random.randint(0,10,size=np.random.randint(3,10)))
        H3.draw('Heap from question 3')
        print('keys in heap:',key_list(H3))
        
    print('Question 4')
    A = [1,3,5,7,9,11,13,15]
    B = [3,6,9,12,15]
    C = [2,4,6,8,10,12,14]

    for L1 in [A,B,C]:
        for L2 in [A,B,C]:
            print('L1=',L1,'L2=',L2)
            print('appears_in_1(L1,L2):', appears_in_1(L1,L2))
    
    
    print('Question 5')
    W = read_words()
    D = first_3_letters(W)

    for p in ['the', 'mil', 'few', 'dat','str']:
        print('words that start with',p,':',D[p])
    
    print('Question 6')
    np.random.seed(0)
    k = [7, 9, 15]
    for i in range(3):
        H6a = build_heap(np.random.randint(0,8,size=np.random.randint(3,10)))
        H6a.draw('Heap from question 6')
        H6b = build_heap(np.random.randint(1,20,size=np.random.randint(3,15)))
        H6b.draw('Heap from question 6')
        print('keys that are less than',k[i])
        print(extract_from_2_heaps(H6a,H6b,k[i]))
        
'''
Question 1
common_chars(data,data): {'d', 't', 'a'}
common_chars(data,structures): {'t'}
common_chars(data,utep): {'t'}
common_chars(data,miners): set()
common_chars(structures,data): {'t'}
common_chars(structures,structures): {'s', 'u', 'c', 'e', 'r', 't'}
common_chars(structures,utep): {'u', 't', 'e'}
common_chars(structures,miners): {'s', 'r', 'e'}
common_chars(utep,data): {'t'}
common_chars(utep,structures): {'u', 't', 'e'}
common_chars(utep,utep): {'e', 'u', 't', 'p'}
common_chars(utep,miners): {'e'}
common_chars(miners,data): set()
common_chars(miners,structures): {'s', 'r', 'e'}
common_chars(miners,utep): {'e'}
common_chars(miners,miners): {'s', 'e', 'm', 'r', 'n', 'i'}
Question 2
S = DATA
Sequence length = 1
The last occurrence of D is in location 0
The last occurrence of A is in location 3
The last occurrence of T is in location 2
Sequence length = 2
The last occurrence of DA is in location 0
The last occurrence of AT is in location 1
Sequence length = 3
The last occurrence of DAT is in location 0
S = ACCAAGGGTTTTGTAGGTGTATACATACCAGGGCAATCGGCAACACGTCTGGTGGAGGTGTGCATAGAACTGCAGTGAGTGTTCGATGTGTGTATTGATAA
Sequence length = 1
The last occurrence of A is in location 100
The last occurrence of C is in location 83
The last occurrence of G is in location 96
The last occurrence of T is in location 98
Sequence length = 2
The last occurrence of AC is in location 68
The last occurrence of CC is in location 27
The last occurrence of GG is in location 56
The last occurrence of TT is in location 94
Sequence length = 3
The last occurrence of ACC is in location 26
The last occurrence of CCA is in location 27
The last occurrence of GGT is in location 56
The last occurrence of TTT is in location 9
Sequence length = 4
The last occurrence of ACCA is in location 26
The last occurrence of CCAA is in location 1
The last occurrence of GGTT is in location 6
The last occurrence of TTTG is in location 9
Sequence length = 5
The last occurrence of ACCAA is in location 0
The last occurrence of CCAAG is in location 1
The last occurrence of GGTTT is in location 6
The last occurrence of TTTGT is in location 9
Question 3
keys in heap: [0, 3, 3, 5, 7, 9, 3]
keys in heap: [1, 4, 2, 6, 8, 8, 7, 6]
keys in heap: [0, 1, 4, 3, 8, 9, 5, 9, 8]
Question 4
L1= [1, 3, 5, 7, 9, 11, 13, 15] L2= [1, 3, 5, 7, 9, 11, 13, 15]
appears_in_1(L1,L2): set()
L1= [1, 3, 5, 7, 9, 11, 13, 15] L2= [3, 6, 9, 12, 15]
appears_in_1(L1,L2): {1, 5, 6, 7, 11, 12, 13}
L1= [1, 3, 5, 7, 9, 11, 13, 15] L2= [2, 4, 6, 8, 10, 12, 14]
appears_in_1(L1,L2): {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
L1= [3, 6, 9, 12, 15] L2= [1, 3, 5, 7, 9, 11, 13, 15]
appears_in_1(L1,L2): {1, 5, 6, 7, 11, 12, 13}
L1= [3, 6, 9, 12, 15] L2= [3, 6, 9, 12, 15]
appears_in_1(L1,L2): set()
L1= [3, 6, 9, 12, 15] L2= [2, 4, 6, 8, 10, 12, 14]
appears_in_1(L1,L2): {2, 3, 4, 8, 9, 10, 14, 15}
L1= [2, 4, 6, 8, 10, 12, 14] L2= [1, 3, 5, 7, 9, 11, 13, 15]
appears_in_1(L1,L2): {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
L1= [2, 4, 6, 8, 10, 12, 14] L2= [3, 6, 9, 12, 15]
appears_in_1(L1,L2): {2, 3, 4, 8, 9, 10, 14, 15}
L1= [2, 4, 6, 8, 10, 12, 14] L2= [2, 4, 6, 8, 10, 12, 14]
appears_in_1(L1,L2): set()
Question 5
words that start with the : ['the', 'they', 'their', 'there', 'them', 'then', 'these', 'themselves', 'theory', 'therefore', 'theater', 'theme', 'therapy', 'theoretical', 'theology', 'thereby', 'therapist', 'theological']
words that start with mil : ['million', 'military', 'milk', 'mild', 'mill']
words that start with few : ['few', 'fewer']
words that start with dat : ['data', 'date', 'database']
words that start with str : ['strong', 'street', 'strategy', 'structure', 'strike', 'strength', 'strange', 'straight', 'struggle', 'stress', 'stretch', 'stream', 'strongly', 'string', 'stranger', 'strategic', 'strip', 'strengthen', 'stroke', 'strict', 'strain', 'structural', 'strictly', 'streak', 'striking', 'straw', 'straighten']
Question 6
keys that are less than 7
[0, 2, 3, 3, 3, 5, 5, 6]
keys that are less than 9
[0, 1, 3, 3, 4, 4, 8]
keys that are less than 15
[1, 1, 1, 4, 11, 12]
'''   

