class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minimum = min(nums)
        count = 0
        for i in nums:
            if i != minimum:
                count = count + i - minimum
        return count