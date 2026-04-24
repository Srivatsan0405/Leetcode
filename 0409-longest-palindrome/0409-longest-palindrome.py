class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        lenght = 0

        for ch in s:
            if ch in seen:
                seen.remove(ch)
                lenght += 2
            else:
                seen.add(ch)    

        if seen:
            lenght += 1

        return lenght            