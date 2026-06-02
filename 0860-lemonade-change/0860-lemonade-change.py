class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        l=[0,0,0]
        for i in bills:
            if(i==5):
                l[0]+=1
            elif(i==10):
                if(l[0]>=1):
                    l[1]+=1
                    l[0]-=1
                else:
                    return False
            else:
                if l[1]>0 and l[0]>0:
                    l[1]-=1
                    l[0]-=1
                elif(l[0]>=3):
                    l[0]-=3
                else:
                    return False
        return True
            
