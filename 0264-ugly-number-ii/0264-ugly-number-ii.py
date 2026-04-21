class Solution:
    def ugly(self, n):
        if n <= 0:
            return False
        
        for i in [2, 3, 5]:
            while n % i == 0:
                n //= i
        
        return n == 1

    def nthUglyNumber(self, n: int) -> int:
        l1 = l2 = l3 = 0
        m2 = 2
        m3 = 3
        m5 = 5
        l = [1]       
        for i in range(1, n):
            un = min(m2, m3, m5)
            l.append(un)        
            if un == m2:
                l1 += 1
                m2 = l[l1] * 2
            if un == m3:
                l2 += 1
                m3 = l[l2] * 3
            if un == m5:
                l3 += 1
                m5 = l[l3] * 5
        return l[-1]