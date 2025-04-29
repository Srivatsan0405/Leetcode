class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == len(set(nums)): return False

        l = 1
        r = l + k
        for i in range(len(nums)):
            if nums[i] in nums[l:r]: return True
            l += 1
            if r < len(nums): r += 1
        return False