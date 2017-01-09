class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a = [0]*26
        for i in s:
            a[ord(i)-97] += 1
        for i in t:
            a[ord(i)-97] -= 1
        
        for i in a:
            if i != 0:
                return False
        return True
        