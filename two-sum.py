class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        indexes = []
        for index, val in enumerate(nums):
            temp = target-val
            if temp in dict:
                indexes = [index ,dict[temp] ]
                break 
            dict[val] = index
        return indexes[::-1] if indexes[0] > indexes[1] else indexes
