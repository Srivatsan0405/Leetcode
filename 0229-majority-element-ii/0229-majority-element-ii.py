
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        l = Counter(nums)
        c1 = c2 = 0
        res1 = res2 = None
        for i in nums:
            if res1 == i:
                c1 += 1
            elif res2 == i:
                c2 += 1
            elif c1 == 0:
                res1 = i
                c1 = 1
            elif c2 == 0:
                res2 = i
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1

        ans = []
        if nums.count(res1) > len(nums) // 3:
            ans.append(res1)
        if res2 is not None and nums.count(res2) > len(nums) // 3:
            ans.append(res2)

        return ans
