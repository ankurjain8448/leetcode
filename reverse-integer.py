class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = int(str(abs(x))[::-1])
        return 0 if len(str(bin(rev))[2:]) > 31 else int(rev) if x > 0 else -int(rev)