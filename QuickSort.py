import numpy as np
import sys
# the setrecursionlimit function is
# used to modify the default recursion
# limit set by python. Using this,
# we can increase the recursion limit
# to satisfy our needs

sys.setrecursionlimit(10 ** 6)

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

A = np.array([5,32,43,9,24,16,2,24,65,50,26,23,99,7])
quickSort(A, 0,13)
print(A)
len(A)


datalist=[]
tmp = np.random.randint(0, 5000,1000000)
#tmp = np.random.randint(0, 5000,1000)
RandomNumber = tmp.copy()

st = time.process_time()
n = len(tmp)-1
quickSort(RandomNumber,0,n)
end = time.process_time()

SortedNumber = RandomNumber.copy()
ReverseNumber = RandomNumber[::-1].copy()

DataSort = [{'Step': 'Random', 'RandomData': tmp, 'SortedData': RandomNumber,'ReverseData':ReverseNumber,'TimeTaken':(end - st)}]
print(DataSort)
datalist.append(DataSort)

st = time.process_time()
quickSort(SortedNumber,0,n)
end = time.process_time()
DataSort = [{'Step': 'Sorted', 'RandomData': tmp, 'SortedData': RandomNumber,'ReverseData':ReverseNumber,'TimeTaken':(end - st)}]
print(DataSort)
datalist.append(DataSort)

st = time.process_time()
quickSort(ReverseNumber,0,n)
end = time.process_time()
DataSort = [{'Step': 'Reverse', 'RandomData': tmp, 'SortedData': RandomNumber,'ReverseData':ReverseNumber,'TimeTaken':(end - st)}]
print(DataSort)
datalist.append(DataSort)

print(datalist[0][0]['Step'],datalist[0][0]['TimeTaken'])
print(datalist[0][0]['Step'],datalist[1][0]['TimeTaken'])
print(datalist[0][0]['Step'],datalist[2][0]['TimeTaken'])