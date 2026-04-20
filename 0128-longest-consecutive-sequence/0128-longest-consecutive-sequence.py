class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = sorted(list(set(nums)))
        res = 1
        m = 1
        i = nums[0]  
        for j in range(1, len(nums)):
            if i + 1 == nums[j]:
                res += 1
                i = nums[j]
            else:
                m = max(m, res)
                res = 1  
                i = nums[j]
        return max(m, res)