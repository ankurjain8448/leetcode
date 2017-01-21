class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        s = (l*(l+1))/2
        return s - sum(nums)
        