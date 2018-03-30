class Solution(object):
	def findMin(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		s = 0
		e = len(nums) - 1
		mid = 0
		while s < e and nums[s] >= nums[e]:
			mid = (s + e)/2
			if nums[mid] < nums[e]:
				e = mid
			elif nums[mid] > nums[s]:
				s = mid + 1 
			else:
				s  += 1
		return nums[s]
