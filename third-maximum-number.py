class Solution(object):
    def mmax(self, keys, max, min):
        for i in xrange(len(keys)):
            if keys[i] == max :
                keys[i] = min
                break
        return keys
    
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        hash_map = {}
        for each in nums:
            if each in hash_map:
                hash_map[each] += 1
            else:
                count += 1
                hash_map[each] = 1
        keys = hash_map.keys()
        if count < 3:
            return max(keys)
        else:
            m = min(keys)
            keys = self.mmax(keys, max(keys), m)
            keys = self.mmax(keys, max(keys), m)
            return max(keys)
