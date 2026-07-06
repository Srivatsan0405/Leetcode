
class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:

        def dfs(cur):
            if cur == s2:
                return 0

            i = 0
            while cur[i] == s2[i]:
                i += 1

            ans = float('inf')

            for j in range(i + 1, len(cur)):
                if cur[j] == s2[i] and cur[j] != s2[j]:
                    nxt = list(cur)
                    nxt[i], nxt[j] = nxt[j], nxt[i]
                    ans = min(ans, 1 + dfs("".join(nxt)))

            return ans

        return dfs(s1)