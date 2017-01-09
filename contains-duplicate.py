class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
        for i in nums:
            i = str(i)
            if i in d :
                return True
            else:
                d[i] = True
        return False
            