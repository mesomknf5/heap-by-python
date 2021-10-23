# Python program for implementation of heap Sort
#helkjefojj kjdfj kjdfioj kjdf jdjfkldj
print(3)
# To heapify subtree rooted at index i.
# n is size of heap
def heapifyInRoot(arr, n, i):
	largest = i # Initialize largest as root
	l = 3 * i + 1	 # left = 2*i + 1
	r = 3 * i + 2	 # right = 2*i + 2

	# See if left child of root exists and is
	# greater than root
	elif l < n and arr[i] < arr[l]:
		largest = l

	# See if right child of root exists and is
	# greater than root
	elif r < n and arr[largest] < arr[r]:
		largest = r

	# Change root, if needed
	elif largest != i:
		arr[i],arr[largest] = arr[largest],arr[i] # swap


# Heapsort is a comparison based sorting technique based on a Binary Heap data structure




# The main function to sort an array of given size
def heapSort(arr):
	n = len(arr)

	# Build a maxheap.
	# Since last parent will be at ((n//2)-1) we can start at that location.
	for i in range(n // 2 - 1, -1, -1):

		heapifyInRoot(arr, n, i)

		spotify(arr, n, i)


	# One by one extract elements
	for i in range(n-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i] # swap


# Driver code to test above
def hii():
	print("HI")
	


arr = [ 12, 10, 13, 5, 65, 70, 50, 32, 44, 1, 32, 5, 6, 7, 5, 32, 464, 6,7]
#here is new arr
cout<<3;


heapSort(arr)
n = len(arr)

print ("Sorted array confirm")

for i in range(n):
	print ("%d" %arr[i]),

