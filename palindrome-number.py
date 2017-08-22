class Solution(object):
    def isPalindrome(self, n):
        """
        :type x: int
        :rtype: bool
        """
        if n < 0:
        	return False
        x = n
        temp = 0
        while n:
        	temp = temp*10 + n%10
        	n /= 10
        return x == temp

obj = Solution()
print obj.isPalindrome(1000021)