class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = 0
    	while n:
    	    c+=1
    	    n = n&(n-1)
    	return c