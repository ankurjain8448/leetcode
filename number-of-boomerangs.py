class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        l = len(points)
        ans = 0
        for i in xrange(l):
            d = {}
            for j in xrange(l):
                if i == j:
                    continue
                d1 = (points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2
                d[d1] = 1 + d.get(d1,0)
            for i in d.values():
                ans = ans + i*(i-1)
        return ans