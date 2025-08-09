class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxsofar=nums[0]
        curmin=nums[0]
        curmax=nums[0]
        for i in range(1,len(nums)):
            n=nums[i]
            if n<0:
                curmin,curmax=curmax,curmin
            curmax=max(n,n*curmax)
            curmin=min(n,n*curmin)
            maxsofar=max(maxsofar,curmax)
        return maxsofar
        