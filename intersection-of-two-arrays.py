class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n1 = {}
        for i in nums1:
            if i in n1:
                n1[i] = True
            else:
                n1[i] = False
        n2 = {}
        for i in nums2:
            if i in n1:
                n2[i] = True
            
        return n2.keys()
        