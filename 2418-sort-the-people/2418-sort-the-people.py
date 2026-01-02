
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d = list(zip(names, heights))
        d.sort(key=lambda x: x[1], reverse=True)
        result = [name for name, height in d]
        return result
