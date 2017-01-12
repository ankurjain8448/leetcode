class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        n = numRows
        if n == 0:
            return []
        elif n == 1:
            return [[1]]
        elif n == 2:
            return [[1],[1,1]]
        a = [[1],[1,1]]
        for i in xrange(2,numRows):
            r = [1]
            for j in xrange(i-1):
                r.append(a[i-1][j] + a[i-1][j+1])
            r.append(1)
            a.append(r)
        return a