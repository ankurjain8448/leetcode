class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        ans = 0
        if num > 0:
            t = num%2
            if t == 0:
                ans = 1
            num /= 2
        else:
            return 0
        p = 1
        while(num):
            p = p << 1
            n = num%2
            if n == 0:
                ans = ans + p
            num /= 2
        
        return ans