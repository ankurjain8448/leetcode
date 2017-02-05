class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0:
            return 0
        i = 0
        start = prices[i]
        end = prices[i]
        ans = 0
        i += 1
        while( i < n ):
            if(prices[i]>prices[i-1]):
                end = prices[i]
            else:
                ans += (end-start)
                start = prices[i]
                end = prices[i]
            i+=1
        if end > start:
            ans += (end-start)
        return ans
            
            