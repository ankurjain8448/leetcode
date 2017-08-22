# class Solution(object):
#     def reverse(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         rev = int(str(abs(x))[::-1])
#         return 0 if len(str(bin(rev))[2:]) > 31 else int(rev) if x > 0 else -int(rev)

class Solution(object):
    def get_rev(self, n):
        temp = 0
        while n:
            rem = n%10
            n /=10
            temp = temp*10 + rem
        if temp > 2**31:
            temp = 0
        return temp

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        return self.get_rev(x) if x >= 0 else -self.get_rev(-x)
