class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n1 = {}
        for i in nums1:
            if i in n1:
                n1[i] += 1
            else:
                n1[i] = 1
        n2 = {}
        for i in nums2:
            if i in n2:
                n2[i] += 1
            else:
                n2[i] = 1
        ans = []
        for k,v in n2.iteritems():
            if k in n1:
                for i in xrange(min(n1[k], v)):
                    ans.append(k)
            
        return ans
        