class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0]*(num+1)
        for i in xrange(1,num+1):
            a = i&(i-1)
            ans[i] = 1 + ans[a]
        return ans