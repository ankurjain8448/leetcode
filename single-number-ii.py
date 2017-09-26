class Solution(object):
	def singleNumber(self, nums, k):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		count = [0 for _ in xrange(64)]
		pos_count = 0
		for n in nums:
			index = 0
			if n >=0:
				pos_count += 1
			temp = abs(n)
			while temp:
				count[index] += (temp & 1)
				temp >>= 1
				index += 1
		result = 0
		for i in xrange(64): 
			result |= ((count[i] % k) << i);
		return result if pos_count%k != 0 else -result

arr = [-2,-2,1,1,-3,1,-3,-3,-4,-2]
each_number_appers_k_times = 3
obj = Solution()
print obj.singleNumber(arr, each_number_appers_k_times)