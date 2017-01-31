class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        a = 0
        for i in xrange(1,l):
            if nums[i] != nums[i-1]:
                a+=1
                nums[a] = nums[i]
        return a+1
        