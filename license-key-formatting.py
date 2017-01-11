class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        arr = []
        ll = []
        str_len = 0
        count_dashes = 0
        for i in s:
            if i != '-':
                ll.append(i.upper())
                str_len += 1
            else:
                count_dashes += 1
            
        chunks = str_len/k
        t = str_len - (chunks)*k
        if t > 0 :
            for i in xrange(t):
                arr.append(ll[i])
            arr.append('-')
                
        for i in xrange(chunks):
            for j in xrange(k):
                arr.append(ll[t + k*i+j])
            arr.append('-')
        if str_len:
            arr.pop()
        return "".join(arr)