class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i=0
        while i<len(matrix):
            if(matrix[i][0]<=target and matrix[i][-1]>=target):
                for j in range(len(matrix[0])):
                    if(matrix[i][j]==target):
                        return True

            elif(matrix[i][0]>=target):
                return False
            
            i+=1
        return False
    
