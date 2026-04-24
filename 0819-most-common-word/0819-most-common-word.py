class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        p=paragraph.lower()
        p = re.sub(r'[^\w\s]', ' ', p)
        c=Counter(p.split())
        for i in banned:
            c.pop(i,None)
        m = max(c, key=c.get)
        return m
