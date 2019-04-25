
#O(nlogn) Space--> O(1)

import time
import random


def parent(i):
	return i//2

def left(i):
	return 2*i + 1

def right(i):
	return 2*i + 2


def heapSort(A):
	n = len(A)
	build_max_heap(A)
	
	for i in range(n-1, -1, -1):
		A[0], A[i] = A[i], A[0]
		n -= 1
		
		max_heapify(A, 0, n)



def max_heapify(A, i, n):
	
	left_child = left(i)
	right_child = right(i)
	
	largest = i 
	
	if left_child < n and A[i] < A[left_child]:
		largest = left_child
		
	if right_child < n and  A[largest] < A[right_child]:
		largest = right_child
		
	if largest != i:
		A[largest], A[i] = A[i], A[largest]
		
		max_heapify(A, largest, n)
		
		
def build_max_heap(A):
	n = len(A)
	m = (n-1) // 2
	for i in range(m, -1, -1):
		max_heapify(A, i, n-1)
		

		


		
def main():
	start_time = time.time()
	A = []
	for i in range (50000):   #change input size to test running time
		A.append(random.randrange(1,1000000,1))
	heapSort(A)
	print("--- %s seconds ---" % (time.time() - start_time))
	#print(A)
	
if __name__ == "__main__":
	main()
