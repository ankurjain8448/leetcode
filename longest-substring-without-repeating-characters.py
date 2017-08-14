class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        start_index = 0
        d  = {}
        for index, val in enumerate(s):
            if val in d:
                old_index = d[val]
                ans = max(ans, len(d))
                for i in xrange(start_index , old_index):
                    d.pop(s[i], None)
                start_index = old_index + 1
                d[val] = index
            else:
                d[val] = index
        ans = max(ans, len(d))
        return ans
        
obj = Solution()
a = "bpfbhmipx"
print obj.lengthOfLongestSubstring(a)