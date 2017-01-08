class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g)
        s = sorted(s)
        g_max = len(g)
        g_index = 0
        for i in xrange(len(s)):
            if s[i] >= g[g_index]:
                g_index += 1
                if g_index == g_max:
                    break
        return g_index