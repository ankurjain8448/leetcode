class Solution(object):
    def uniquePaths(self, rows, cols):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        arr = [ 1 for j in xrange(cols)]
        for i in xrange(rows-1):
        	for j in xrange(1, cols):
        		arr[j] += arr[j-1]
        return arr[cols-1]
