class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        flag = True
        
        in_b = set(['[', '(', '{'])
        for i in s:
            if i in in_b:
                stack.append(i)
            else:
                if len(stack):
                    v = stack.pop()
                    if i == ']':
                        if v != '[':
                            return False
                    elif i == ')':
                        if v != '(':
                            return False
                    else:
                        if v != '{':
                            return False
                else:
                    return False
        if len(stack):
            flag = False
        return flag
