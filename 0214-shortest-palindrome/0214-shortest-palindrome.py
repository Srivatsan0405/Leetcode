class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        
        c = len(s)
        
        while c > 0:
            if s[:c] == s[:c][::-1]:
                break
            c -= 1
        
        return s[c:][::-1] + s