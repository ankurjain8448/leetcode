class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I':1,'IV' : 4 , 'V':5,'IX' : 9 , 'X':10, 'XL' : 40 , 'L' : 50,'XC' : 90 , 'C' : 100, 'CD': 400 , 'D' : 500,'CM' : 900 , 'M' : 1000}
        l = len(s)
        ans = 0
        i = 0
        while (i<l):
            if(i+1 < l) and s[i]+s[i+1] in d :
                ans += d[s[i]+s[i+1]]
                i += 1
            else:
                ans += d[s[i]]
            i += 1
        return ans