class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p=0
        Mincost=prices[0]
        for i in range(1,len(prices)):
            if(prices[i]-Mincost>p):
                p=prices[i]-Mincost
            if(prices[i]<Mincost):
                Mincost=prices[i]
        return p
            
        