from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        p = [1] * (n + 1)
        pre = [0] * (n + 1)
        cnt = [0] * (n + 1)
        num = [0] * (n + 1)

        for i in range(1, n + 1):
            p[i] = (p[i - 1] * 10) % MOD

        for i in range(n):
            t = int(s[i])
            pre[i + 1] = pre[i] + t

            if t != 0:
                cnt[i + 1] = cnt[i] + 1
                num[i + 1] = (num[i] * 10 + t) % MOD
            else:
                cnt[i + 1] = cnt[i]
                num[i + 1] = num[i]

        l = []

        for i in queries:
            left = i[0]
            right = i[1]

            c = cnt[right + 1] - cnt[left]

            res = (num[right + 1] - num[left] * p[c]) % MOD
            sm = pre[right + 1] - pre[left]

            l.append((res * sm) % MOD)

        return l