class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        l = len(nums)/2
        for i in nums:
            i = str(i)
            if i in d:
                d[i] += 1
                if d[i] > l:
                    return int(i)
            else:
                d[i] = 1
                if d[i] > l:
                    return int(i)