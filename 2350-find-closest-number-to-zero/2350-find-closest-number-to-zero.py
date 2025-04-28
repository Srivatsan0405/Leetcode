class Solution:
    def findClosestNumber(self, A):
        return max([-abs(a), a] for a in A)[1] 


        