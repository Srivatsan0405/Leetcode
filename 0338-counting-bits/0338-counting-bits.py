class Solution:
    def countBits(self, n: int) -> List[int]:
        l=[]
        for i in range(n+1):
            c=0
            a=bin(i)
            for j in a:
                if(j=='1'):
                    c+=1
            l.append(c)
        return l