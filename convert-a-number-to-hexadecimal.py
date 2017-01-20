class Solution(object):
    def toHex(self, n):
        """
        :type num: int
        :rtype: str
        """
        if n == 0:
            return '0'
        a = ['a','b','c','d','e','f']
        if n < 0:
            n = 2**32 + n
        ans = []
        while n:
            temp = n%16
            if temp <10 :
                ans.append(str(temp))
            else:
                ans.append(a[temp-10])
            n = n/16
        ans = ans[::-1]
        return "".join(ans)