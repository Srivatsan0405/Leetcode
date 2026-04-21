class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        num=[]
        for i in nums:
            num.append(int(str(i)[::-1]))
        s=set(num+nums)
        return len(s)
