class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        arr = [0]*(n+1)
        i = n-1
        j = n
        carry = 1
        while i >=0:
        	carry += digits[i]
        	arr[j] = carry%10
        	carry /= 10
        	i -= 1
        	j -= 1
        if carry:
        	arr[j] = carry
        i = 0
        n = len(arr)
        while i<n:
        	if arr[i] != 0:
        		return arr[i:]
        	i += 1
        return arr

obj = Solution()
a = [1,8]
print obj.plusOne(a)