import numpy as no

def BubleSort(arr):
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

A = np.array([5,32,43,9,24,16,2,24,65,50,26,99])
BubleSort(A)
print(A)



datalist=[]
datalist2=[]

tmp = np.random.randint(0, 5000,1000000)
tmp = np.random.randint(0, 5000,1000)
RandomNumber = tmp.copy()

st = time.process_time()
BubleSort(RandomNumber)
end = time.process_time()

SortedNumber = RandomNumber.copy()
ReverseNumber = RandomNumber[::-1].copy()

DataSort = [{'Step': 'Random', 'RandomData': tmp, 'SortedData': RandomNumber,'ReverseData':ReverseNumber,'TimeTaken':(end - st)}]
print(DataSort)
datalist.append(DataSort)

st = time.process_time()
BubleSort(SortedNumber)
end = time.process_time()
DataSort = [{'Step': 'Sorted', 'RandomData': tmp, 'SortedData': RandomNumber,'ReverseData':ReverseNumber,'TimeTaken':(end - st)}]
print(DataSort)
datalist.append(DataSort)

st = time.process_time()
BubleSort(ReverseNumber)
end = time.process_time()
DataSort = [{'Step': 'Reverse', 'RandomData': tmp, 'SortedData': RandomNumber,'ReverseData':ReverseNumber,'TimeTaken':(end - st)}]
print(DataSort)
datalist.append(DataSort)

print(datalist[0][0]['TimeTaken'])
print(datalist[1][0]['TimeTaken'])
print(datalist[2][0]['TimeTaken'])