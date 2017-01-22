class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        flag = True
        a = []
        for i in s:
            t = i.lower()
            i = ord(t)
            if (i > 96 and i < 123) or (  i > 47  and i < 58 ) :
                a.append(t)
        l = len(a)
        for i in xrange(l/2):
            if a[i] != a[l-1-i]:
                flag = False
                break
        return flag