class Solution(object):

    def lengthOfLongestSubstring(self, s, k):
        """
        s : input String
        k : longest-substring-with-at-most-k-different-characters
        Time Complexity : O(n)
        Space Complexity : O(k)
        """
        ans = 0
        start_index = 0
        d  = {}
        for index, val in enumerate(s):
            if val in d:
                d[val].append(index)
            else:
                if len(d) > k-1:
                    ans = max(ans, sum(len(v) for v in d.values()))
                    keys = d.keys()
                    min_key = keys[0]
                    for each in keys:
                        if d[each][-1] < d[min_key][-1]:
                            min_key = each
                    d.pop(min_key, None)
                d[val] = [index]

        ans = max(ans, sum(len(v) for v in d.values()))
        return ans
        
obj = Solution()
a = "eceba"
print obj.lengthOfLongestSubstring(a, 3)