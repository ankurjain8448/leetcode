class Solution(object):
	def findMin(self, arr):
		"""
		:type arr: List[int]
		:rtype: int
		"""
		if len(arr) < 4:
			return min(arr)
		s = 0
		e = len(arr) - 1
		while s < e and arr[s] >= arr[e]:
			mid = (s + e) / 2
			if arr[s] > arr[mid]:
				e = mid
			elif arr[e] < arr[mid]:
				s = mid + 1
		return arr[s]

a = [1]
print Solution().findMin(a)