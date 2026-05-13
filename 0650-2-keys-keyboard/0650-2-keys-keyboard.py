class Solution:
    def minSteps(self, n: int) -> int:
        i=2
        ans=0
        while n!=1:
            if(n%i==0):
                n=n/i
                ans+=i
            else:
                i+=1
        return(ans)


        