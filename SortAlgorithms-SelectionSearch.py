
import numpy as np
A = np.array([5,32,43,9,24,16,2,24,65,50,26])

print(len(A))

print(SelectionSort(A))
print(selection_sort(A))
print(SelectionSortHW(A))

def SelectionSort(A):
    n=len(A)
    for i in range (n-1) :
        min = i
        for j in range(i+1, n-1):
            if A[j] < A[min]:
                min = j
        tmp = A[i]
        A[i] = A[min]
        A[min] = tmp
    return (A)


def selection_sort(arr):
    for i in range(len(arr)):
        minimum = i
        for j in range(i + 1, len(arr)):
            # Select the smallest value
            if arr[j] < arr[minimum]:
                minimum = j
        # Place it at the front of the
        # sorted end of the array
        arr[minimum], arr[i] = arr[i], arr[minimum]
    return arr




def SelectionSortHW(arr):
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if A[j] < A[min]:
                min = j
        A[min],A[i] = A[i],A[min]
    return (arr)

def InsertionSortHW(arr):
    n = len(arr)
    for i in range(n):
        tmp = arr[i]
        #for j in range(i, 0 , -1):
        j = i
        #for j in range(i, 0, -1) & tmp < arr[j-1]:
        while (j> 0 and tmp < arr[j-1]):
            arr[j] = arr[j-1]
            j = j-1
        arr[j] = tmp
    return (arr)

def BubleSortHW(arr):
    sortedStatus = False
    last = len(arr)-1
    i=0
    while (i < last and sortedStatus==False):
        sortedStatus = True
        for j in range(last,i,-1):
            if arr[j-1] > arr[j]:
                arr[j-1],arr[j] = arr[j],arr[j-1]
                sortedStatus = False
        i = i + 1
    return (arr)

from random import randint

Arandom = np.random.randint(100, size=10)

A = np.array([5,32,43,9,24,16,2,24,65,50,26])
print(InsertionSortHW(Arandom))

A = np.array([5,32,43,9,24,16,2,24,65,50,26])
print(BubleSortHW(Arandom))



def mergeSortHW1(arr,first,last):
    print("Splitting ",arr)
    #if len(arr)>1:
    if first<last :
        mid = (first + last) //2
        #mid = len(arr)//2
        lefthalf = arr[first , mid]
        righthalf = arr[mid+1,last]
        #mergeSortHW1(lefthalf)
        #mergeSortHW1(righthalf)
        mergeSortHW1(arr,first,mid)
        mergeSortHW1(arr, mid+1, last)
        merge(arr,first,mid,last)
        #mergeHW(arr, lefthalf, righthalf)

A = np.array([5,32,43,9,24,16,2,24,65,50,26])
mergeSortHW1(A,0,10)
print(A)

def mergeHW1(nlist, lefthalf, righthalf):
    i = j = k = 0

    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            nlist[k] = lefthalf[i]
            i = i + 1
        else:
            nlist[k] = righthalf[j]
            j = j + 1
        k = k + 1

    while i < len(lefthalf):
        nlist[k] = lefthalf[i]
        i = i + 1
        k = k + 1

    while j < len(righthalf):
        nlist[k] = righthalf[j]
        j = j + 1
        k = k + 1

nlist = [14,46,43,27,57,41,45,21,90]
mergeSortHW1(nlist,0,8)
print(nlist)


def Merge(arr,first,mid,last):
    first1=first
    last1=mid
    first2=mid+1
    last2=last
    index=first1
    tempArray=[]
    theArray=[]
    i11 = j11 = 0
    k11 = mid
    while (first1 <= last1) and (first2 <= last2):
        if theArray[first1]<theArray[first2]:
            tempArray[k11] = theArray[first1]
            i11 = i11 + 1
        else:
            tempArray[k11] = theArray[first2]
            j11 = j11 + 1
        k11 = k11 + 1

    while i11 <= last1:
        tempArray[k11] = theArray[first1]
        first1 = first1+1
        k11 = k11 + 1

    while j11 <= last2:
        tempArray[k11] = theArray[first2]
        first2 = first2+1
        k11 = k11 + 1
    print(tempArray)
#    j3 = first
#    while (k11<=last):
#            theArray[j3] = tempArray[j3]
#            j3 = j3 + 1
        #for index in range (first,last,1):
        #    theArray[index] = tempArray[index]


def MergeSort(arr, first, last):
    if first < last:
        mid = (first + last) / 2
        mid = (first + (last-1)) // 2
        #m = (l + (r - 1)) // 2
        MergeSort(arr, first, mid)
        MergeSort(arr, mid+1, last)
        Merge(arr, first, mid, last)

A = np.array([5,32,43,9,24,16,2,24,65,50,26])
MergeSort(A,0,10)
print(A)

def mergeSortHW(arr):
    print("Splitting ",arr)
    if len(arr)>1:
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]
        mergeSortHW(lefthalf)
        mergeSortHW(righthalf)
        mergeHW(arr, lefthalf, righthalf)

def mergeHW(nlist, lefthalf, righthalf):
    i = j = k = 0

    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            nlist[k] = lefthalf[i]
            i = i + 1
        else:
            nlist[k] = righthalf[j]
            j = j + 1
        k = k + 1

    while i < len(lefthalf):
        nlist[k] = lefthalf[i]
        i = i + 1
        k = k + 1

    while j < len(righthalf):
        nlist[k] = righthalf[j]
        j = j + 1
        k = k + 1

nlist = [14,46,43,27,57,41,45,21,70]
mergeSortHW(nlist)
print(nlist)

first = 0
last =10
print((first+last)/2)

A = np.array([5,32,43,9,24,16,2,24,65,50,26])
MergeSort(A, 1,11)

A = np.array([5,32,43,9,24,16,2,24,65,50,26])
mergeSort(A,0,10)
print(A)

# Python program for implementation of MergeSort
# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

        # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# l is for left index and r is right index of the
# sub-array of arr to be sorted
def mergeSort(arr, l, r):
    if l < r:
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = (l + (r - 1)) // 2
        m = (l + r) // 2
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)
A = np.array([5,32,43,9,24,16,2,24,65,50,26])
mergeSort(A,0,10)
print(A)


def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot
    for j in range(low, high):
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

A = np.array([5,32,43,9,24,16,2,24,65,50,26])
quickSort(A, 0,10)
print(A)


def mergeSort(nlist):
    print("Splitting ",nlist)
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",nlist)

nlist = [14,46,43,27,57,41,45,21,70]
mergeSort(nlist)