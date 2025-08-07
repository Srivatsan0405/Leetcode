class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        a=0
        heights.append(0)
        stack=[-1]
        for i,h in enumerate(heights):
            while stack[-1]!=-1 and heights[stack[-1]]>h:
                a=max(a,heights[stack.pop()]*(i-stack[-1]-1))
            stack.append(i)
        return a
        