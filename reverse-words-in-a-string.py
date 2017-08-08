class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        start_index = 0
        end_index = len(s) - 1
        while start_index < end_index and s[start_index] == ' ':
            start_index += 1
        while start_index < end_index and s[end_index] == ' ':
            end_index -= 1
        if start_index == end_index and s[start_index] == ' ':
            return ""
        temp_end = end_index
        temp_start = end_index
        arr = []
        while temp_start > start_index:
            char = s[temp_start]
            if char == ' ':
                if temp_end - temp_start > 0:
                    arr.append(s[temp_start+1:temp_end+1] + ' ')
                temp_end = temp_start
                temp_end -= 1
            temp_start -= 1
        if temp_end - temp_start >= 0:
            arr.append(s[temp_start:temp_end+1])
        return ''.join(arr)
