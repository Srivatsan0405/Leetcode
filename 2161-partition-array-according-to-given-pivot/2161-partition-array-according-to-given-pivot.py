class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        low=[]
        hig=[]
        p=[]
        for i in nums:
            if i<pivot:
                low.append(i)
            elif i==pivot:
                p.append(i)
            else:
                hig.append(i)
        return low+p+hig