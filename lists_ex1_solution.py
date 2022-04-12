# Solutions to list exercises
# Report errors to ofuentes@utep.edu

def all_equal(L):
    if len(L)>1:
        for item in L[1:]:
            if item!=L[0]:
                return False
    return True

def greater_than_x(L,x):
    G = []
    for item in L:
        if item>x:
            G.append(item)
    return G

def greater_than_x_lc(L,x):
    return [i for i in L if i>x]

def split_even_odd_index(L):
    even,odd= [], []
    for i in range(0,len(L),2):
        even.append(L[i])
    for i in range(1,len(L),2):
        odd.append(L[i])
    return even, odd

def split_even_odd_index_s(L):
    return L[::2],L[1::2]

def split_even_odd(L):
    even,odd= [], []
    for i in L:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return even, odd

def split_even_odd_lc(L):
    return [x for x in L if x % 2 == 0], [x for x in L if x % 2 == 1]

def split_middle(L):
    mid = len(L)//2
    return L[:mid], L[mid:]

def split_pivot(L):
    left, right = [],[]
    if len(L)>0:
        pivot = L[0]
        for i in L:
            if i < pivot:
                left.append(i)
            else:
                right.append(i)
    return left, right

def split_pivot_lc(L):
    if len(L)==0:
        return [], []
    return [item for item in L if item<L[0]],[item for item in L if item>=L[0]]

if __name__ == "__main__":

    L1 = [6, 4, 8, 9, 1, 3, 7, 5, 2, 0]
    L2 = [40, 60,10,20,30,80,50]
    L3 = [3,1,2]
    L4 = [18, 0, 12, 9, 6, 15, 3]
    L5 = []
    L6 = [2302]

    print('Question 1')
    print(all_equal([]))
    print(all_equal([5]))
    print(all_equal([3,3,2,3,3]))
    print(all_equal([3,3,3,3,4]))
    print(all_equal([3,3,3,3,3,3]))

    print('Question 2')
    Ls = [2,5,7,1,2,5,7,8,9,0]
    for x in [4,9,-1,7]:
        print('x =',x)
        print(greater_than_x(Ls,x))

    print('Question 3')
    Ls = [2,5,7,1,2,5,7,8,9,0]
    for x in [4,9,-1,7]:
        print('x =',x)
        print(greater_than_x_lc(Ls,x))

    print('Question 4')
    for L in [L1,L2,L3,L4,L5,L6]:
        La,Lb = split_even_odd_index(L)
        print(La,Lb)

    print('Question 5')
    for L in [L1,L2,L3,L4,L5,L6]:
        La,Lb = split_even_odd_index_s(L)
        print(La,Lb)

    print('Question 6')
    for L in [L1,L2,L3,L4,L5,L6]:
        La,Lb = split_even_odd(L)
        print(La,Lb)

    print('Question 7')
    for L in [L1,L2,L3,L4,L5,L6]:
        La,Lb = split_even_odd_lc(L)
        print(La,Lb)

    print('Question 8')
    for L in [L1,L2,L3,L4,L5,L6]:
        La,Lb = split_middle(L)
        print(La,Lb)

    print('Question 9')
    for L in [L1,L2,L3,L4,L5,L6]:
        La,Lb = split_pivot(L)
        print(La,Lb)

    print('Question 10')
    for L in [L1,L2,L3,L4,L5,L6]:
        La,Lb = split_pivot_lc(L)
        print(La,Lb)

'''
Expected output:
Question 1
True
True
False
False
True
Question 2
x = 4
[5, 7, 5, 7, 8, 9]
x = 9
[]
x = -1
[2, 5, 7, 1, 2, 5, 7, 8, 9, 0]
x = 7
[8, 9]
Question 3
x = 4
[5, 7, 5, 7, 8, 9]
x = 9
[]
x = -1
[2, 5, 7, 1, 2, 5, 7, 8, 9, 0]
x = 7
[8, 9]
Question 4
[6, 8, 1, 7, 2] [4, 9, 3, 5, 0]
[40, 10, 30, 50] [60, 20, 80]
[3, 2] [1]
[18, 12, 6, 3] [0, 9, 15]
[] []
[2302] []
Question 5
[6, 8, 1, 7, 2] [4, 9, 3, 5, 0]
[40, 10, 30, 50] [60, 20, 80]
[3, 2] [1]
[18, 12, 6, 3] [0, 9, 15]
[] []
[2302] []
Question 6
[6, 4, 8, 2, 0] [9, 1, 3, 7, 5]
[40, 60, 10, 20, 30, 80, 50] []
[2] [3, 1]
[18, 0, 12, 6] [9, 15, 3]
[] []
[2302] []
Question 7
[6, 4, 8, 2, 0] [9, 1, 3, 7, 5]
[40, 60, 10, 20, 30, 80, 50] []
[2] [3, 1]
[18, 0, 12, 6] [9, 15, 3]
[] []
[2302] []
Question 8
[6, 4, 8, 9, 1] [3, 7, 5, 2, 0]
[40, 60, 10] [20, 30, 80, 50]
[3] [1, 2]
[18, 0, 12] [9, 6, 15, 3]
[] []
[] [2302]
Question 9
[4, 1, 3, 5, 2, 0] [6, 8, 9, 7]
[10, 20, 30] [40, 60, 80, 50]
[1, 2] [3]
[0, 12, 9, 6, 15, 3] [18]
[] []
[] [2302]
Question 10
[4, 1, 3, 5, 2, 0] [6, 8, 9, 7]
[10, 20, 30] [40, 60, 80, 50]
[1, 2] [3]
[0, 12, 9, 6, 15, 3] [18]
[] []
[] [2302]
'''