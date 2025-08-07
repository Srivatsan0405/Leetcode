class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted(set([n for n in nums if n > 0]))
        target = 1
        for n in nums:
            if n == target:
                target += 1
            elif n > target:
                break
        return target
