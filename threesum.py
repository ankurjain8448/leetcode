class Solution(object):
	def threeSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		n = len(nums)
		d = {}
		ans = []
		old = set()
		for index, value in enumerate(nums):
			if value not in d:
				d[value] = set()
			d[value].add(index)
		for i in xrange(n):
			for j in xrange(i+1, n):
				temp = -(nums[i] + nums[j])
				if temp in d:
					ff = d[temp]
					ff = list(ff - set([i,j]))
					if len(ff):
						tt = sorted([nums[i], nums[j], nums[ff[0]]])
						ss = "_".join(map(str, tt))
						if ss not in old:
							old.add(ss)
							ans.append(tt)
		return ans
