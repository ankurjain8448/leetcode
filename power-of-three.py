class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        flag = True
        if n < 1:
            return False
        m = 3**19
        if m%n == 0 :
            return True
        return False