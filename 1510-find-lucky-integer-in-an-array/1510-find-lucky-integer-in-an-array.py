class Solution:
    def findLucky(self, arr: List[int]) -> int:
        s=set(arr)
        l=[]
        res=0
        for i in s:
            c=arr.count(i)
            l.append([i,c])
        for i in range(len(l)):
            if(l[i][0]==l[i][1]):
                res=l[i][0]
        if res==0:
            return -1
        return res
                
            
            

        