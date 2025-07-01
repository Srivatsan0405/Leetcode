class Solution(object):
    def nearestPalindromic(self, n):
        k = len(n)
        p = int(n[:(k + 1) // 2])
        c = {
            str(10**k + 1),
            str(10**(k - 1) - 1)
        }
        for i in [p - 1, p, p + 1]:
            s = str(i)
            if k % 2 == 0:
                pal = s + s[::-1]
            else:
                pal = s + s[:-1][::-1]
            c.add(pal)
        c.discard(n)
        return min(c, key=lambda x: (abs(int(x) - int(n)), int(x)))