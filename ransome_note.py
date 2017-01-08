class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        arr = [0]*256
        for i in magazine:
            arr[ord(i)] += 1
        for i in ransomNote:
            ii = ord(i)
            if arr[ii] == 0:
                break
            arr[ii] -= 1
        else:
            return True
        return False
            
        # d = {}
        # for i in magazine:
        #     if i in d:
        #         d[i] += 1
        #     else:
        #         d[i] = 1
        # flag = True
        # for i in ransomNote:
        #     if i in d:
        #         if d[i] > 0:
        #             d[i] -= 1
        #         else:
        #             flag = False
        #             break
        #     else:
        #         flag = False
        #         break
        # return flag
                
        