class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        s=0
        for i in operations:
            if i=="--X" or i=='X--':
                s=s-1
            else:
                s=s+1
        return s

            