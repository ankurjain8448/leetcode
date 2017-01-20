class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = 0
        l = len(prices)
        if l == 0 :
            return ans
        min_arr = [prices[0]]
        for i in xrange(1,l):
            min_arr.append(min(prices[i],min_arr[i-1]))

        temp_max = prices[l-1]
        ans = max(ans,temp_max - min_arr[l-1])
        for i in xrange(l-2,-1,-1):
            temp_max = max(temp_max,prices[i])
            ans = max(ans,temp_max - min_arr[i])
        return ans
        