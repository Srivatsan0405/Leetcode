class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        i=j=0
        res=[]
        while i<len(matrix):
            j=0
            ans=0
            while j<len(matrix[0]):
                ans+=matrix[i][j]
                j+=1
            res.append(ans)
            i+=1

        return res


