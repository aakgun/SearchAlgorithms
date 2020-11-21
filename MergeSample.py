
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
    k = l
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



def mergeSortHW1(arr,first,last):
    print("Splitting ",arr)
    #if len(arr)>1:
    if first<last:
        mid = (first + last) //2
        mergeSortHW1(arr,first,mid)
        mergeSortHW1(arr, mid+1, last)
        #merge(arr,first,mid,last)
        Merge(arr, first, mid, last)
        #mergeHW(arr, lefthalf, righthalf)

A = np.array([5,32,43,9,24,16,2,24,65,50,26])
mergeSortHW1(A,0,10)
print(A)

A = np.array([5,32,43,9,24,16,2,24,65,50,26])
mergeSort(A,0,10)
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





##########################

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