from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        
        n = len(nums)
        ans = float('inf')
        
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] == nums[j] == nums[k]:
                        ans = min(ans,abs(i - j) + abs(j - k) + abs(i - k))        
        return ans if ans != float('inf') else -1