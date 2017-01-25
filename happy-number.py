class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        a = set()
        a.add(n)
        while True:
        	temp = 0
        	while n:
        		temp += (n%10)**2
        		n /= 10
        	if temp == 1:
        		return True
        	if temp in a:
        		return False
        	n = temp
        	a.add(n)