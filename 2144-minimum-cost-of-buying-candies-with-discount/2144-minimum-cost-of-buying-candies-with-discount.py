class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        c=0
        res=0
        for i in reversed(cost):
            if(c==2):
                c=0
            else:
                res+=i
                c+=1
        return(res)
            

    