class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = set(word)
        c = 0

        for ch in range(ord('a'), ord('z') + 1):
            lower = chr(ch)
            upper = chr(ch).upper()
            if lower in s and upper in s:
                c += 1
        return c