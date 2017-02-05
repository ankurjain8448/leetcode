class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
        	return 0
        ans = nums[0]
        temp = nums[0]
        for i in xrange(1,n):
        	temp = max(nums[i] , temp+nums[i])
        	ans = max(temp, ans)
        return ans