class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        res=0
        piles.sort(reverse=True)
        for i in range(1,2*(len(piles) // 3),2):
           res+=piles[i]
        return res

            