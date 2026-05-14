class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """    
        c = 0   
        for i in range(len(nums) - 1): 
            if nums[i] > nums[i + 1]:
                c += 1
                if c > 1:
                    return False
                if i > 0 and nums[i - 1] > nums[i + 1]:
                    nums[i + 1] = nums[i]
                else:
                    nums[i] = nums[i + 1]
        
        return True