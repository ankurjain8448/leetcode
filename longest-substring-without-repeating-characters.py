class Solution(object):
    def remove(self, s, dict, index):
        m = min(dict.values())
        for i in xrange(m , index):
            if s[i] in dict:
                dict.pop(s[i])

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        d  = {}
        for index, val in enumerate(s):
            if val in d:
                old_index = d[val]
                ans = max(ans, len(d))
                self.remove(s, d, old_index)
                d[val] = index
            else:
                d[val] = index
        ans = max(ans, len(d))
        return ans
        
obj = Solution()
a = "a"
print obj.lengthOfLongestSubstring(a)