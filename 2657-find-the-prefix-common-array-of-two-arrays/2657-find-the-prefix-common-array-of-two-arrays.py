class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        c=[0]*len(A)
        for i in range(len(A)):
            for j in range(i+1):
                if(A[j] in B[:i+1]):
                    c[i]+=1
        return(c)

