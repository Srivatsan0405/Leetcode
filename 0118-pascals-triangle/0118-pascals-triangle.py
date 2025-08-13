class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for num in range(numRows):
            num = [1]
            if res:
                last = res[-1]
                for i in range(1,len(last)):
                    num.append(last[i-1] + last[i])
                num.append(1)
            res.append(num)
        return res