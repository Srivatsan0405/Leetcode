

class Solution:

    def isPrime(self, x: int) -> bool:
        if x < 2:
            return False
        if x == 2:
            return True
        if x % 2 == 0:
            return False
        d = 3
        while d * d <= x:
            if x % d == 0:
                return False
            d += 2
        return True
    def diagonalPrime(self, l: List[List[int]]) -> int:
        n = len(l)
        i = 0
        m = 0
        while i < n:
            if self.isPrime(l[i][i]):
                m = max(m, l[i][i])
            if i != n-1-i and self.isPrime(l[i][n-1-i]):
                m = max(m, l[i][n-1-i])
            i += 1
        return m
