class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        val = int(-1 + int(math.sqrt(1+ 8*n)))/2
        return val