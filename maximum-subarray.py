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
        temp_ans = nums[0]
        for i in xrange(1,n):
        	temp_ans = max(nums[i] , temp_ans+nums[i])
        	ans = max(temp_ans, ans)
        return ans