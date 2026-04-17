class Solution:
    def reverse(self, n):
        t = 0
        while n > 0:
            t *= 10
            t += n % 10
            n //= 10
        return t

    def minMirrorPairDistance(self, nums):
        mp = {}
        ans = float('inf')

        n = len(nums)
        mp[nums[n - 1]] = n - 1

        for i in range(n - 2, -1, -1):
            rev = self.reverse(nums[i])

            if rev in mp:
                j = mp[rev]
                ans = min(ans, j - i)

            mp[nums[i]] = i

        return -1 if ans == float('inf') else ans