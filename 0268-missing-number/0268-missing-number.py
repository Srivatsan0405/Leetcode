class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        target=0
        nums = sorted(nums)
        for i in nums:
            if target==i:
                target+=1
            else:
                return target

        return target