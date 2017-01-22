class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # check 2**n form
        n = num
        if n == 0 :
            return False
        if n & (n-1) == 0:
            return True
        two = 0
        three = 0
        five = 0
        while n > 1:
            ff = True
            if n%2 == 0 :
                ff = False
                n /= 2
                two += 1

            if n%3 == 0:
                ff = False
                n /= 3
                three += 1
            
            if n%5 == 0:
                ff = False
                n /= 5
                five += 1
            
            if ff :
                break
        nn = 1
        if two > 0:
            nn  *= 2**two
        if three > 0 :
            nn *= 3**three
        if five > 0:
            nn *= 5**five
        if nn == num:
            return True
        return False