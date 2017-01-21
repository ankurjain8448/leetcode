class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        a = [True]*(n)
        a[0] = False
        a[1] = False
        t = 2
        while t*t < n :
            t += 1
        for i in xrange(2,t):
            j = 2*i
            if a[i] :
                while(j < n):
                    a[j] = False
                    j += i
        c = 0
        for i in xrange(n):
            if a[i] :
                c += 1
        return c