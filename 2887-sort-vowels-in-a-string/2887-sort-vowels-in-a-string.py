class Solution:
    def sortVowels(self, s: str) -> str:
        l=[]
        t=""
        j=0
        for i in s:
            if i in "AEIOUaeiou":
                l.append(i)
        l.sort()
        for i in s:
            if i in "AEIOUaeiou":
                t=t+l[j]
                j+=1
            else:
                t=t+i
        return (t)


