class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        s=0
        c=0
        for i in events:
            if(c==10):
                break
            elif(i.isdigit()):
                s+=int(i)
            elif(i=='W'):
                c+=1
            else:
                s+=1
        return [s,c]
            

