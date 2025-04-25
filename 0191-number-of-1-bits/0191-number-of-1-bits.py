class Solution:
    def hammingWeight(self, n: int) -> int:
        n1=bin(n)
        c=0
        for i in n1:
            if(i=='1'):
                c+=1
        return(c)