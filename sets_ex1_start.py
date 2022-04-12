import matplotlib.pyplot as plt
import numpy as np

def sum_of_two(L,s):
    # T(n) = O(n)
    setSeen=set()
    for i in L:
        for j in setSeen:
            if j+i==s:
                return [j, i]
        setSeen.add(i)
    return []

def repeated_sequences(S,n):
    # T(n) = O(n)
    repeated = set()
    seen_once = set()
    for i in range(len(S)-n+1):
        if S[i:i+n] in seen_once:
            repeated.add(S[i:i+n])
        seen_once.add(S[i:i+n])
    return list(repeated)

if __name__ == "__main__":

    plt.close('all')

    print('Question 1')
    L = [1, 2, 5, 14, 6, 7, 8 ]
    print('L=',L)
    for s in range(2*max(L)):
        print('s =',s,'   sum_of_two(L,s) =',sum_of_two(L,s))

    S = 'ACCAAGGGTTTTGTAGGTGTATACATACCAGGGCAATCGGCAACACGTCTGGTGGAGGTGTGCATAGAACTGCAGTGAGTGTTCGATGTGTGTATTGATAA'

    print('Question 2')
    for n in range(1,8):
        print('Sequence length =',n)
        print('Repeated sequences:',repeated_sequences(S,n))

'''
Question 1
L= [1, 2, 5, 14, 6, 7, 8]
s = 0    sum_of_two(L,s) = []
s = 1    sum_of_two(L,s) = []
s = 2    sum_of_two(L,s) = []
s = 3    sum_of_two(L,s) = [1, 2]
s = 4    sum_of_two(L,s) = []
s = 5    sum_of_two(L,s) = []
s = 6    sum_of_two(L,s) = [1, 5]
s = 7    sum_of_two(L,s) = [2, 5]
s = 8    sum_of_two(L,s) = [2, 6]
s = 9    sum_of_two(L,s) = [2, 7]
s = 10    sum_of_two(L,s) = [2, 8]
s = 11    sum_of_two(L,s) = [5, 6]
s = 12    sum_of_two(L,s) = [5, 7]
s = 13    sum_of_two(L,s) = [6, 7]
s = 14    sum_of_two(L,s) = [6, 8]
s = 15    sum_of_two(L,s) = [1, 14]
s = 16    sum_of_two(L,s) = [2, 14]
s = 17    sum_of_two(L,s) = []
s = 18    sum_of_two(L,s) = []
s = 19    sum_of_two(L,s) = [5, 14]
s = 20    sum_of_two(L,s) = [14, 6]
s = 21    sum_of_two(L,s) = [14, 7]
s = 22    sum_of_two(L,s) = [14, 8]
s = 23    sum_of_two(L,s) = []
s = 24    sum_of_two(L,s) = []
s = 25    sum_of_two(L,s) = []
s = 26    sum_of_two(L,s) = []
s = 27    sum_of_two(L,s) = []
Question 2
Sequence length = 1
Repeated sequences: ['A', 'G', 'T', 'C']
Sequence length = 2
Repeated sequences: ['TT', 'CT', 'AT', 'CC', 'CA', 'AA', 'TC', 'CG', 'GA', 'GT', 'AG', 'AC', 'GG', 'GC', 'TA', 'TG']
Sequence length = 3
Repeated sequences: ['GAT', 'CCA', 'CAA', 'CAT', 'AGG', 'GCA', 'TTG', 'TGT', 'AGT', 'TGA', 'GTG', 'CTG', 'GTA', 'TTT', 'ACA', 'GGC', 'TAG', 'GGG', 'TGG', 'TGC', 'TCG', 'AAC', 'CAG', 'ACC', 'GAG', 'TAT', 'ATA', 'GTT', 'TAC', 'GGT']
Sequence length = 4
Repeated sequences: ['AGGG', 'TGTA', 'GGCA', 'TGTG', 'AGGT', 'CATA', 'GGTG', 'AGTG', 'TGCA', 'GTAT', 'GCAA', 'GTGT', 'ATAC', 'ACCA']
Sequence length = 5
Repeated sequences: ['GTGTA', 'GTGTG', 'TGTAT', 'TGTGT', 'AGGTG', 'GGCAA', 'GGTGT']
Sequence length = 6
Repeated sequences: ['AGGTGT', 'GTGTAT']
Sequence length = 7
Repeated sequences: []
'''