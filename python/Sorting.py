
# Traverse through all  elements 
def selection_sort(A):
    for i in range(len(A)-1,0,-1):
        #print(i)
        maxIndex=0
        for j in range(1, i+1):
            if A[j]>A[maxIndex]:
                maxIndex=j
        A[i],A[maxIndex]=A[maxIndex],A[i]
A=[7,6,5,8,4,9,67,88]
selection_sort(A)
print(A)

#insertion sort

def insertion_sort(B):
    for i in range(1,len(B)):
        currrentVal=B[i]
        position=i

        while position>0 and B[position-1]>currentVal:
            B[position]=A[position-1]
            position=position-1
        B[position]=currentVal
B=[7,6,5,8,4,9,67,88]

print("insertion ",B)

def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
    

     while index>0 and alist[index-1]>currentvalue:
         alist[index]=alist[index-1]
         index = index-1

     alist[index]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)
#selection
arr = [5,4,3,1,6,8,10,9] # array not sorted
for i in range(len(arr)):
    for j in range(i, len(arr)):
        if(arr[i] > arr[j]):
            arr[i], arr[j] = arr[j], arr[i]
print (arr)
