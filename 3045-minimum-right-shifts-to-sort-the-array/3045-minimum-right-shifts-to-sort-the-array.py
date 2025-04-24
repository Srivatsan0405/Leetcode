class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        def check(arr):
            for i in range(len(arr) - 1):
                if arr[i] >= arr[i + 1]:
                    return False
            return True
        n = len(nums)
        for k in range(n):
            if check(nums):
                return k
            nums = nums[-1:] + nums[:-1]
        return -1
