import numpy as np

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


def Merge(arr,l,m,r):
    #first1=l
    #last1=m
    #first2=m+1
    #last2=r
    #index=first1
    #tempArray=[]
    #theArray=[]

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

    i = 0
    j = 0
    k = 1
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    #while (first1 <= last1) and (first2 <= last2):
    #    if theArray[first1]<theArray[first2]:
    #        tempArray[k11] = theArray[first1]
    #        i11 = i11 + 1
    #    else:
    #        tempArray[k11] = theArray[first2]
    #        j11 = j11 + 1
    #    k11 = k11 + 1

    #while i <= last1:
    while i < n1:
        #tempArray[k11] = theArray[first1]
        arr[k] = L[i]
        i += 1
        k += 1
        #i = i+1
        #first1 = first1+1
        #k = k + 1

    #while j11 <= last2:
    while j < n2:
        #tempArray[k11] = theArray[first2]
        arr[k] = R[j]
        j += 1
        k += 1
        #first2 = first2+1
        #j = j+1
        #k = k + 1
    #print(tempArray)


def Merge2(arr,l,m,r):

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


def mergeSortHW1(arr,first,last):
    print("Splitting ",arr)
    #if len(arr)>1:
    if first<last:
        mid = (first + last) //2
        mergeSortHW1(arr,first,mid)
        mergeSortHW1(arr, mid+1, last)
        #merge(arr,first,mid,last)
        #Merge(arr, first, mid, last)
        Merge2(arr, first, mid, last)
        #mergeHW(arr, lefthalf, righthalf)

A = np.array([5,32,43,9,24,16,2,24,65,50,26])
mergeSortHW1(A,0,10)
print(A)