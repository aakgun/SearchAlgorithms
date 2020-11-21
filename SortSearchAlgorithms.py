import numpy as np

A = np.array([5,32,43,9,24,16,2,24,65,50,26])

print(len(A))


print(selection_sort(A))
print(SelectionSort2(A))




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




def SelectionSort2(arr):
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if A[j] < A[min]:
                min = j
        A[min],A[i] = A[i],A[min]
    return (arr)


A = np.array([89,45,68,90,29,34,17])
def BinarySearch (arr,K):
    l = 0
    h = len(arr)
    notfound = True
    while l < h and notfound==True:
        mid = (l + h) // 2
        if arr[mid] == K:
            notfound = False
            return mid
        if arr[mid] < K:
            l = mid+1
        elif arr[mid] > K:
            h = mid-1


print(BinarySearch(A,43))




import numpy as np

A = np.array([89, 45, 68, 90, 29, 34, 17])
print(len(A))

def InsertionSort(arr):
    i=1
    for i in range(1,len(arr)):
        tmp = arr[i]
        j = i-1
        print(i)
        while j >= 0 and A[j] > tmp:
            print("j:{0} A[j]:{1} tmp:{2} A[j+1]:{3}".format(j, A[1], tmp, A[j+1]))
            A[j+1] = A[j]
            j=j-1
            print("END j:{0} A[j]:{1} tmp:{2} A[j+1]:{3}".format(j, A[1], tmp, A[j + 1]))
        A[j+1] = tmp
        print("END j:{0} A[j]:{1} tmp:{2} A[j+1]:{3}".format(j, A[1], tmp, A[j + 1]))
    return arr

print(InsertionSort(A))

def SelectionSort(A):
    n=len(A)
    for i in range (n-2) :
        min = i
        for j in range(i+1, n-1):
            if A[j] < A[min]:
                min = j
        tmp = A[i]
        A[i] = A[min]
        A[min] = tmp
    return (A)

print(SelectionSort(A))

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

A = np.array([5,32,43,9,24,16,2,24,65,50,26])
BubleSortHW(A)
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


#############

import time
import numpy as np
import matplotlib.pyplot as plt


def maxheap(a, i):
    l = 2 * i
    r = 2 * i + 1
    n = len(a) - 1
    if (l <= n and a[l] > a[i]):
        large = l
    else:
        large = i
    if (r <= n and a[r] > a[large]):
        large = r
    if (large != i):
        temp = a[i]
        a[i] = a[large]
        a[large] = a[i]
        maxheap(a, large)


def build_heap(a):
    leaf = int(len(a) / 2)
    for i in range(leaf - 1, -1, -1):
        maxheap(a, i)


def heapsort(a):
    build_heap(a)
    n = len(a) - 1
    for i in range(int(n), 0, -1):
        a[i], a[0] = a[i], a[0]  # easy way to swap elements directly
        n = n - 1
        maxheap(a, 0)


A = np.array([5,32,43,9,24,16,2,24,65,50,26])
heapsort(A)
print(A)

a = np.random.randint(0, 1 * 5000, 1 * 1000)
B = heapsort(a)

print(a)

dict1 = {}  # using dictionary to store the time taken by each set of elements
for i in range(1, 10):
    a = np.random.randint(0, i * 5000, i * 1000)
    st = time.process_time()
    heapsort(a)
    end = time.process_time()
    dict1[len(a)] = (end - st)
    print("Time taken by " + str(len(a)) + " numbers is " + str(dict1[len(a)]))
print("Following graph depicts the Time Complexity plot for heap sort:")
plt.xlabel("Elements in a heap")
plt.ylabel("Time")
plt.title("Heap Sort Time Complexity")
plt.plot(*zip(*sorted(dict1.items())))
plt.show()

############################################3


a = np.random.randint(0, 1 * 5000, 1 * 1000)
B = heapSort(a)



def heapify(arr, n, i):
	largest = i # Initialize largest as root
	l = 2 * i 	 # left = 2*i + 1
	r = 2 * i + 1	 # right = 2*i + 2

	# See if left child of root exists and is
	# greater than root
	if l < n and arr[i] < arr[l]:
		largest = l

	# See if right child of root exists and is
	# greater than root
	if r < n and arr[largest] < arr[r]:
		largest = r

	# Change root, if needed
	if largest != i:
		arr[i],arr[largest] = arr[largest],arr[i] # swap

		# Heapify the root.
		heapify(arr, n, largest)

# The main function to sort an array of given size
def heapSort(arr):
	n = len(arr)

	# Build a maxheap.
	for i in range(n, -1, -1):
		heapify(arr, n, i)

	# One by one extract elements
	for i in range(n-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i] # swap
		heapify(arr, i, 0)

a = A = np.array([5,32,43,9,24,16,2,24,65,50,26])# np.random.randint(0, 1 * 5000, 1 * 1000)
heapSort(a)
print(a)

datalist=[]
datalist2=[]

dict1 = {}  # using dictionary to store the time taken by each set of elements
for i in range(1, 10):
    a = np.random.randint(0, i*5000,i*1000)
    st = time.process_time()
    tmp=a.copy()
    heapSort(a)
    end = time.process_time()
    dict1[len(a)] = (end - st)
    DataSort=[{'Step':i,'RandomData':tmp,'SortedData':a}]
    DataSort1 = [[i, tmp,  a]]
    datalist.append(DataSort)
    datalist2.append(DataSort1)
    print("{0}.Step: Array: {1} : Sorted array {2}",i, tmp, a)
    print("Time taken by " + str(len(a)) + " numbers is " + str(dict1[len(a)]))
print("Following graph depicts the Time Complexity plot for heap sort:")
plt.xlabel("Elements in a heap")
plt.ylabel("Time")
plt.title("Heap Sort Time Complexity")
plt.plot(*zip(*sorted(dict1.items())))
plt.show()


datalist=[]
datalist2=[]

tmp = np.random.randint(0, 5000,1000000)
RandomNumber = tmp.copy()

st = time.process_time()
heapSort(RandomNumber)
end = time.process_time()

SortedNumber = RandomNumber.copy()
ReverseNumber = RandomNumber[::-1].copy()

DataSort = [{'Step': 'Random', 'RandomData': tmp, 'SortedData': RandomNumber,'ReverseData':ReverseNumber,'TimeTaken':(end - st)}]
print(DataSort)
datalist.append(DataSort)

st = time.process_time()
heapSort(SortedNumber)
end = time.process_time()
DataSort = [{'Step': 'Random', 'RandomData': tmp, 'SortedData': RandomNumber,'ReverseData':ReverseNumber,'TimeTaken':(end - st)}]
print(DataSort)
datalist.append(DataSort)

st = time.process_time()
heapSort(ReverseNumber)
end = time.process_time()
DataSort = [{'Step': 'Random', 'RandomData': tmp, 'SortedData': RandomNumber,'ReverseData':ReverseNumber,'TimeTaken':(end - st)}]
print(DataSort)
datalist.append(DataSort)

#dict1[len(RandomNumber)] = (end - st)
#DataSort = [{'Step': 'Random', 'RandomData': tmp, 'SortedData': RandomNumber,'ReverseData':ReverseNumber,'TimeTaken':(end - st)}]
#DataSort1 = [[i, tmp, a]]



print(tmp)
print(SortedNumber)
print(ReverseNumber)
datalist[0]

print(RandomNumber[::-1])

datalist[0]

datalist[0][0]['SortedData']