class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        s=str(n)
        if(x==int(s[0])):
            return False
        if(str(x) in s):
            return True
        return False