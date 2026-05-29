class Solution:
    def digsum(self,n):
        r=0
        while n:
            r+=n%10
            n//=10
        return r

    def minElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i]=self.digsum(nums[i])
        return(min(nums))
    
        