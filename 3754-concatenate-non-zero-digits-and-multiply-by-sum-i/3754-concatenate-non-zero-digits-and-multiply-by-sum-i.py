class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s=0
        num=0
        while n>0:
            
            t=n%10
            if(t!=0):
                num*=10
                s+=t
                num+=t

            n=n//10
            
            
        res=(int(str(num)[::-1]))
        return res*s

