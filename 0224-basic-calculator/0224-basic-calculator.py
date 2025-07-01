class Solution(object):
    def calculate(self, s):
        res, num, sign = 0, 0, 1
        stack = []
        
        for c in s + '+':
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in '+-':
                res += sign * num
                sign = 1 if c == '+' else -1
                num = 0
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                res, sign = 0, 1
            elif c == ')':
                res += sign * num
                res *= stack.pop()   
                res += stack.pop()    
                num = 0
        
        return res