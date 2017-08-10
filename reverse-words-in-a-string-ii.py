class Solution(object):
    def reverse(self, s , start, end):
        while start<end:
            s[start], s[end] = s[end], s[start]
            start+=1 
            end -=1

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        start_index = 0
        end_index = 0
        s = [i for i in s]
        for i in s:
            if i == ' ':
                self.reverse(s, start_index, end_index-1)
                start_index = end_index + 1
                end_index = start_index
            else:
                end_index += 1
        if start_index < end_index :
            self.reverse(s, start_index, end_index-1)

        self.reverse(s, 0, len(s) - 1)
        return "".join(s)
obj = Solution()
print obj.reverseWords('abcd hkds bhdb bpdfdb x')