class Solution(object):
    def readBinaryWatch(self, n):
        """
        :type num: int
        :rtype: List[str]
        """
        hh = {}
        mm = {}
        for i in xrange(0,60):
            hh[i] = []
            mm[i] = []
            temp = i
            counter = 0
            while temp :
                temp = temp & (temp-1)
                counter += 1
            if i < 12:
                i = str(i)
                hh[counter].append(i)
            i = str(i)
            if len(i) == 1:
                i = "0"+i
            mm[counter].append(i)

        ans = set()
        for i in xrange(n+1):
            h = i
            m = n - i
            hour_values = hh[h]
            minute_values = mm[m]
            if len(hour_values) < 1:
                break
            for p in hour_values:
                for q in minute_values:
                    ans.add(str("%s:%s" % (p,q)))
        return list(ans)