class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c = {}
        m = 0 
        l = 0
        res = 0

        for r in range(len(s)):
            c[s[r]] = c.get(s[r], 0) + 1
            m = max(m, c[s[r]])
            while (r - l + 1) - m > k:
                c[s[l]] -= 1
                l += 1

            res = max(m, r - l + 1)

        return res