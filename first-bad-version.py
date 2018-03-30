# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = 1
        e = n
        index = -1
        while s <= e:
            mid = (s+e)/2
            if isBadVersion(mid):
                index = mid
                e = mid - 1
            else:
                s = mid + 1
        return index
