class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        res=0
        c=0
        for i in moves:
            if(i=='L'):
                res+=1
            elif(i=='R'):
                res-=1
            else:
                c+=1
        if(res>=0):
            res+=c
        else:
            res-=c
        return abs(res)

