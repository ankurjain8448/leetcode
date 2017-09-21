class Solution(object):
	def singleNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		a = nums[0]
		for i in nums[1:]:
			a ^= i
		return a
