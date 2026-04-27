class Solution:
    def maxProduct(self, n: int) -> int:
        l=[]
        for i in str(n):
            l.append(int(i))
        l.sort()
        return l[-1]*l[-2]