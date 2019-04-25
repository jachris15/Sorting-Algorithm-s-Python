#O(n^2) worst case, avg case O(nlogn) Space --> O(1), most commonly used 


import random
import time 


def QuickSort(A, p, r):
	if p < r:
		q = partition(A, p, r)
	
		QuickSort(A, p, q-1)
		QuickSort(A, q+1, r)
	



def partition(A, p, r):
	
	i = (p-1)
	x = A[r]
	
	for j in range(p,r):
		if A[j] <= x:
			i += 1
			A[i], A[j] = A[j], A[i]
			
	A[i+1], A[r] = A[r], A[i+1]
	return(i + 1)









def main():
	start_time = time.time()
	A = []
		
	for i in range (50000): #change input size to test running time
		A.append(random.randrange(1,1000000,1))
		
	QuickSort( A, p = 0, r = len(A)-1)
	print("--- %s seconds ---" % (time.time() - start_time))
	#print(A)


if __name__ == "__main__":
	main()
