class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        m=nums[-1]
        if(m+1!=len(nums)):
            return False
        for i in range(1,m+1):

            if(i!=nums[i-1]):
                return False
        return True
