class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(int(c**0.5) + 1): 
            j = int((c - i**2)**0.5)  
            if i**2 + j**2 == c:
                return True
        return False
