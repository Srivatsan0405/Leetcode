class Solution:
    def check(self, nums: List[int]) -> bool:
        arr=copy.deepcopy(nums)
        nums.sort()
        n=len(nums)
        for i in range(n):
            if arr==nums:
                return True
            nums=nums[1:]+nums[:1]
        return False
    

        