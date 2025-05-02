class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split()
        s1=" ".join(l[::-1])
        return s1
        