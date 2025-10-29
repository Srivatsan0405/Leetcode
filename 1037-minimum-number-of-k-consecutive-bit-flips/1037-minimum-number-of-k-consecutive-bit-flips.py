class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flip = 0
        c = 0
        flipped = [0] * n
        for i in range(n):
            if i >= k:
                flip ^= flipped[i - k]
            if nums[i] ^ flip == 0:
                if i + k > n:
                    return -1
                c += 1
                flip ^= 1
                flipped[i] = 1
        return c
