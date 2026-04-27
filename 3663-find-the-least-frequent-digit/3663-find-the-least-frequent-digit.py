class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        d=str(n)
        c=Counter(d)
        m=min(c.values())
        dic=c.items()
        l=[]
        print(dic)
        for i,j in dic:
            if(j==m):
                l.append(int(i))
        return min(l)