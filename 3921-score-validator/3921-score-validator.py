class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        l=[0,0]
        for i in events:
            if(l[1]==10):
                break
            elif(i.isdigit()):
                l[0]+=int(i)
            elif(i=='W'):
                l[1]+=1
            else:
                l[0]+=1
        return l
            

