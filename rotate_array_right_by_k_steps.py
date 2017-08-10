'''
	Rotate an array to the right by k steps in-place without allocating extra space. For
	instance, with k = 3, the array [0, 1, 2, 3, 4, 5, 6] is rotated to [4, 5, 6, 0, 1, 2, 3].
'''
def rotate(arr, k):
	'''
		rType : list
	'''
	n = len(arr)
	if k >= n:
		k = k % n
	next_element = arr[0]
	next_index = k
	if k == 0:
		return arr
	for i in xrange(n):
		temp = arr[next_index]
		arr[next_index] = next_element
		next_index = (next_index + k)%n
		next_element = temp
	return arr


arr = [0, 1, 2, 3, 4, 5, 6]
k = 3
print rotate(arr, k)