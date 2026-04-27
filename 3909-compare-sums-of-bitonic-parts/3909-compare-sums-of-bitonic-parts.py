class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        m=nums.index(max(nums))
        al=nums[m]
        dl=nums[m]
        for i in range(len(nums)):
            if(i<m):
                al+=nums[i]
            if(i>m):
                dl+=nums[i]
        print(al,dl)
        if(al==dl):
            return -1
        elif(al>dl):
            return 0
        else:
            return 1

        