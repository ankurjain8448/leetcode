class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operand = []
        for i in tokens :
            try:
                i = int(i)
                operand.append(i)
            except :
                b = operand.pop()
                a = operand.pop()
                t = ''
                if i == '/':
                    if a*b <0:
                        a = abs(a)
                        b = abs(b)
                    t = a/b
                elif i == '+':
                    t  = a+b
                elif i == '-':
                    t = a-b
                else :
                    t = a*b
                operand.append(t)
            print operand
        return operand[0]


exp = ["4", "13", "5", "/", "+"]
exp = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print Solution().evalRPN(exp)