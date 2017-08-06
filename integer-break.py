class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 1
        for i in xrange(2, n):
            q = n/i
            r = n%i
            if r :
                ans = max(ans, (i**q)*r )
                if q != 1:
                    ans = max(ans, (i**(q-1))*(i+r))
            else:
                ans = max(ans, i**q)    
        return ans
