class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        min_diff = area
        temp_l = area
        l = 1
        while l*l < area:
            l += 1
        while l > 0 :
            if area % l == 0:
                w = area/l
                diff = abs(w-l)
                if diff < min_diff:
                    min_diff = diff
                    temp_l = l
                if l <= w:
                    break
            l -= 1
        return sorted([area/temp_l,temp_l])[::-1]