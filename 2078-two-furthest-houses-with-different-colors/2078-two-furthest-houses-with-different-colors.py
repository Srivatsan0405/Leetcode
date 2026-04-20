class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        res=[]
        for i in range(len(colors)):
            for j in range(i,len(colors)):
                if(colors[i]!=colors[j]):
                    res.append(abs(i-j))
        return max(res)