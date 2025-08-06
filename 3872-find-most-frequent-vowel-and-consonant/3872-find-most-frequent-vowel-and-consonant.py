class Solution:
    def maxFreqSum(self, s: str) -> int:
        se = set(s)
        v = []
        const = []

        for i in se:
            c = s.count(i)
            if i in 'aeiou':
                v.append(c)
            else:
                const.append(c)
        v1 = max(v) if v else 0
        c1 = max(const) if const else 0
        res = v1 + c1
        return res
