class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        s=set()
        for i in bulbs:
            if i in s:
                s.remove(i)
            else:
                s.add(i)
        l=list(s)
        l.sort()
        return l