class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        s = 0
        e = len(numbers)-1
        while s < e :
            t = numbers[s] + numbers[e]
            if t == target:
                break
            elif t > target :
                e -= 1
            else:
                s += 1
        return [s+1, e+1]