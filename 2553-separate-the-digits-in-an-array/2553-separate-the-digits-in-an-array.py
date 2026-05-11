class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        l=[]
        for i in nums:
            s=0
            for j in str(i):
                l.append(int(j))
        return(l)

