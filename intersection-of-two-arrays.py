class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n1 = {}
        for i in nums1:
            n1[i] = True if i in n1 else False
        return list({ i for i in nums2 if i in n1 })
        