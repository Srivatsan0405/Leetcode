class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        from functools import lru_cache
        s = set(words)

        @lru_cache(None)
        def can(w):
            for i in range(1, len(w)):
                if w[:i] in s and (w[i:] in s or can(w[i:])):
                    return True
            return False

        return [w for w in words if (s.remove(w), can(w), s.add(w))[1]]
