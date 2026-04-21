class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        res=0
        d=str(digit)
        for i in nums:
            res+=str(i).count(d)
        return res