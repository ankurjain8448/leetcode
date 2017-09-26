class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        a = [0]*32
        temp = n
        i = 31
        while n:
            a[i] = n&1
            n = n >> 1
            i -= 1
        p = 1
        ans = 0
        for i in a:
            ans = ans + i*p
            p = p << 1
        return ans