from typing import List
import matplotlib.pyplot as plt
import numpy as np

def count_occurrences(L):
    D ={}
    for i in L:
        if i in D:
            D[i] += 1
        else:
            D[i] = 1
    return D

def find_occurrences(L):
    D ={}
    for i in range(len(L)):
        if L[i] in D:
            D[L[i]] += [i]
        else:
            D[L[i]]=[i]
    return D

def word_rank_dictionary(word_list):
    D ={}
    for i in range(len(word_list)):
        if word_list[i] not in D.keys():
            D[word_list[i]] = i+1
    return D

def find_anagrams(L):
    D ={}
    setL=set()
    for i in L:
        if ''.join(sorted(i)) not in setL:
            setL.add(''.join(sorted(i)))
    for i in setL:
        for j in L:
            if i in D and i == ''.join(sorted(j)):
                D[i]+=[j]
            elif i == ''.join(sorted(j)):
                D[i]=[j]
    return D

if __name__ == "__main__":

    np.random.seed(0)
    L = np.random.permutation(100)[:40]%20
    print(L)

    D = count_occurrences(L)
    for i in set(L):
        print('item {} appears {} times in list'.format(i,D[i]))

    D = find_occurrences(L)
    for i in set(L):
        print('item',i,'appears in positions',D[i],'in list')

    word_list = []
    with open('most_common_words.txt') as f:
        for line in f:
            word_list.append(line[:-1])

    word_rank_D = word_rank_dictionary(word_list)

    for word in ['them','the','data','structure','python','a','algorithm']:
        if word in word_rank_D.keys():
            d = word_rank_D[word]
            print('The word -',word,'- ranks',d,'among the most common words in the English language.')
        else:
            print('The word -',word,'- is not among the most common words in the English language.')

    D = find_anagrams(word_list)
    m = 3
    print('Anagram sets with {} or more members:'.format(m))
    for w in D:
        if len(D[w])>=m:
            print('key:',w,'- anagram list:',D[w])

'''
[ 6  6  2 15 15 13 16 13 14 15 13 12 18 13  7 10  2  4 13  8  3  2  3 11
  5  8  6 19  2 16  0  0 10  8 11  7 18 16  3 14]
item 0 appears 2 times in list
item 2 appears 4 times in list
item 3 appears 3 times in list
item 4 appears 1 times in list
item 5 appears 1 times in list
item 6 appears 3 times in list
item 7 appears 2 times in list
item 8 appears 3 times in list
item 10 appears 2 times in list
item 11 appears 2 times in list
item 12 appears 1 times in list
item 13 appears 5 times in list
item 14 appears 2 times in list
item 15 appears 3 times in list
item 16 appears 3 times in list
item 18 appears 2 times in list
item 19 appears 1 times in list
item 0 appears in positions [30, 31] in list
item 2 appears in positions [2, 16, 21, 28] in list
item 3 appears in positions [20, 22, 38] in list
item 4 appears in positions [17] in list
item 5 appears in positions [24] in list
item 6 appears in positions [0, 1, 26] in list
item 7 appears in positions [14, 35] in list
item 8 appears in positions [19, 25, 33] in list
item 10 appears in positions [15, 32] in list
item 11 appears in positions [23, 34] in list
item 12 appears in positions [11] in list
item 13 appears in positions [5, 7, 10, 13, 18] in list
item 14 appears in positions [8, 39] in list
item 15 appears in positions [3, 4, 9] in list
item 16 appears in positions [6, 29, 37] in list
item 18 appears in positions [12, 36] in list
item 19 appears in positions [27] in list
The word - them - ranks 55 among the most common words in the English language.
The word - the - ranks 1 among the most common words in the English language.
The word - data - ranks 512 among the most common words in the English language.
The word - structure - ranks 859 among the most common words in the English language.
The word - python - is not among the most common words in the English language.
The word - a - ranks 5 among the most common words in the English language.
The word - algorithm - is not among the most common words in the English language.
Anagram sets with 3 or more members:
key: aemt - anagram list: ['team', 'meat', 'mate']
key: opst - anagram list: ['stop', 'spot', 'post']
key: ader - anagram list: ['read', 'dear', 'dare']
key: opt - anagram list: ['top', 'pot', 'opt']
key: lost - anagram list: ['lots', 'lost', 'slot']
key: deit - anagram list: ['diet', 'tide', 'edit']
key: aelp - anagram list: ['pale', 'leap', 'plea']
'''
