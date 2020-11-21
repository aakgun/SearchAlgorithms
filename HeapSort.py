
import numpy as np

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
