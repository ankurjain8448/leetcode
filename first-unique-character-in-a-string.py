class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = [0]*256
        for i in s:
            a[ord(i)] += 1
        index = -1
        for k,i in enumerate(s):
            if a[ord(i)] == 1:
                index = k
                break
            
        return index
        