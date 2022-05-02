def min_index(lst):
    
    k = 0
    for i in range(1, len(lst)):
        if lst[i] < lst[k]:
            k = i
    return lst[k]


print(min_index([6,4,67,7]))

def selection_sort(lst):
    for i in range(len(lst)):
        j = min_index(lst[i:]) + i
        lst[i], lst[j] = lst[j], lst[i]
    return lst[i]

#print(selection_sort([6,89,67,5]))

import re

def tokenization(exp):
    math_re = re.compile(r"(\(*\)*-*\+*\**\^* *)")
    tokenized = re.split(math_re, exp)
    tokenized = [x for x in tokenized if x not in [" ", ""]]
    for i, item in enumerate(tokenized):
        try:
            tokenized[i] = item.replace(" ", "")
            item = float(item)
            tokenized[i] = item
        except ValueError:
            pass
    return tokenized

print(tokenization("(3.1 + 6*2^2) * (2 - 1)"))

def minimum_spanning_tree(graph):
    tree = empty_graph(len(graph))
    con = [0]
    while len(con) < len(graph):
        i, j = min_extension(con, graph)
        tree[i][j], tree[j][i] = graph[i][j], graph[j][i]
        con += [j]
    return tree
def min_extension(con, g):
    min_weight=inf
    for i in con:
        for j in range(len(g)):
            if j not in con and 0<g[i][j ]< min_weight:
                v, w = i, j
                min_weight = g[i][j]
    return i, j


def sequential_search(v, seq):
    n = len(seq)
    i = 0
    while i < n:
        if seq[i] == v:
            return seq[i]
        if seq[i]>v:
            return None
        i += 1
    return None
print(sequential_search(10,(1,2,3,4,5,3,4,5,3,4,5,8,9,10)))
      
def probing_search(v, seq):
    a= 0
    b=len(seq)-1
    while a<=b:
        c=(a+b)//2
        if seq[c] == v:
            return seq[c]
        elif v < seq[c]:
            b = c - 1
        else:
            a = c + 1
print(probing_search(20,(5,10,15,20,25,30,35,40,45,50,55)))

def probing_search2(v, seq):
    a, b = 0, len(seq)-1
    c = b // 2
    if seq[c] == v:
        return c
    elif v < seq[c]:
        b = c - 1
    else:
        a = c + 1
print(probing_search2(20,(5,10,15,20,25,30,35,40,45,50,55)))

def merge_sort(A):
    merge_sort2(A,0,len(A)-1) #recursive function with starting and ending index
    
def merge_sort2(A,first,last):
    if first<last:#more than 1 item
        middle=(first+last)//2
        merge_sort2(A,first,middle)
        merge_sort2(A,middle+1,last)
        merge(A,first,middle,last)

def merge(A,first,middle,last):
    L=A[first:middle]
    R=A[middle:last+1]
    L.append(999999999)
    R.append(999999999)
    i=j=0
    for k in range (first,last+1):
        if L[i]<=R[j]:
            A[k]=L[i]
            i+=1
        else:
            A[k]=R[j]
            j+=1
    return A
A=[1222,667,33,223,78,5444,332,7788,56,43,8,9]
print(merge_sort(A))            
    
