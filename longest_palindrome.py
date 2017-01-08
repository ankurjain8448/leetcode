class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = [False]*150
        count = 0
        for i in s :
            index = ord(i)
            if a[index] :
                count += 2
                a[index] = False
            else:
                a[index] = True
        if any(a):
            count += 1
        return count
