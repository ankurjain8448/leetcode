class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = nums[0]
        minimum = nums[0]
        # curr_max = maximum
        actual_max = maximum
        for i in nums[1:]:
            old_max = maximum
            old_min = minimum
            maximum = max(i, old_max*i, old_min*i)
            minimum = min(i, old_max*i, old_min*i)
            actual_max = max(actual_max, maximum)
        return actual_max
                
                
        