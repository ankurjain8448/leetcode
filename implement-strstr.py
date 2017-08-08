class Solution(object):
    def calculate_phi(self, a):
        n = len(a)
        phi = [0]*n
        for i in xrange(1, n):
            j = i
            while j > 0 and a[i] != a[phi[j-1]]:
                j = phi[j-1]
            if a[i] == a[phi[j-1]]:
                phi[i] = phi[j-1] + 1
            else:
                phi[i] = j
        return phi
    
    def kmp(self, text, pattern):
        phi = self.calculate_phi(pattern)
        i = 0 # text index
        j = 0 # pattern index
        n = len(text)
        pattern_len = len(pattern)
        while i < n:
            if text[i] == pattern[j]:
                i += 1
                j += 1
                if j == pattern_len:
                    return i - pattern_len
            else:
                if j == 0:
                    i += 1
                else:
                    j = phi[j-1]
        return -1
    
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        m = len(needle)
        if n > 0 and m > 0:
            return self.kmp(haystack, needle)
        else:
            if m == 0:
                return 0
        return -1
