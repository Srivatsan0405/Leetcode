import math

class Solution:
    
    def isprime(self, n):
        if n <= 1:
            return False
        
        if n == 2:
            return True
        
        if n % 2 == 0:
            return False
        
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        
        return True

    
    def sumOfPrimesInRange(self, n: int) -> int:
        
        e = int(str(n)[::-1])
        
        start = min(n, e)
        end = max(n, e)
        
        s = 0
        
        for i in range(start, end + 1):
            if self.isprime(i):
                s += i
        
        return s