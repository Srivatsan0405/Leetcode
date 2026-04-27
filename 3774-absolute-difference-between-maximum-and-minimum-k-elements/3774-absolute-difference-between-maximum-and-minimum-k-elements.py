class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        mx=0
        mn=0
        for i in range(k):
            mn+=nums[i]
            mx+=nums[-(i+1)]
        return mx-mn
