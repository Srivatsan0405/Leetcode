class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[-1]
        maxnum=0
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack)==0:
                    stack.append(i)
                else:
                    maxnum=max(maxnum,i-stack[-1])
        return maxnum
