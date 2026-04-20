class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        j=1
        m=0

        while j<len(nums):
            m=max(m,nums[j]-nums[i])
            i+=1
            j+=1
        return m
            
