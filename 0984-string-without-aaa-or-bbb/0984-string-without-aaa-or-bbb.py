class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        s = ""
        while a > 0 or b > 0:
            if a > b:
                x = min(2, a)
                s += 'a' * x
                a -= x
                if b > 0:
                    s += 'b'
                    b -= 1
            elif b > a:
                x = min(2, b)
                s += 'b' * x
                b -= x
                if a > 0:
                    s += 'a'
                    a -= 1
            else:
                if a > 0:
                    s += 'a'
                    a -= 1
                if b > 0:
                    s += 'b'
                    b -= 1
        return s