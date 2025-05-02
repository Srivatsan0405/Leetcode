class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        ss=s1.split()
        ss1=s2.split()
        ss+=ss1
        c = Counter(ss)
        l=[]
        for i,j in c.items():
            if(j==1):
                l.append(i)
        return l
                