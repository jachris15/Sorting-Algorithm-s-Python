
#O(nlogn) Space--> O(n)




import time
import random

def MergeSort(A, low, high):
	#print(low)
	#print(high)
	if low < high:
		mid = (low + high) // 2
		
		MergeSort(A, low, mid)
		MergeSort(A, mid +1, high)
		merge(A, low, mid, high)



def merge( A, low, mid, high):
	B = A[low:mid+1]
	C = A[mid+1:high+1]
	i = 0
	j = 0
	k = low
	
	while i < len(B) and j<len(C):
		if B[i] < C[j]:
			A[k] = B[i]
			i += 1
		else:
			A[k] = C[j]
			j += 1
		k += 1
	
	while i < len(B):
		A[k] = B[i]
		i += 1
		k += 1
		
	while j < len(C):
		A[k] = C[j]
		j += 1
		k += 1
		
	
		

def main():
	start_time = time.time()
	A =[]
	for i in range (50000):  #change input size to test running time
		A.append(random.randrange(1,1000000,1))
	
	newArray = MergeSort(A, low = 0, high = len(A)-1)
	print("--- %s seconds ---" % (time.time() - start_time))
	#print(A)


if __name__ == "__main__":
	main()
