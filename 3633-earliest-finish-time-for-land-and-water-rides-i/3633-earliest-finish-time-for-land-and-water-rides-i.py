from typing import List

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int],
                           waterStartTime: List[int], waterDuration: List[int]) -> int:
        res = float('inf')
        for t in range(len(landStartTime)):
            m = landStartTime[t] + landDuration[t]
            for s in range(len(waterStartTime)):
                n = max(m, waterStartTime[s])
                res = min(res, n + waterDuration[s])
        for t in range(len(waterStartTime)):
            m = waterStartTime[t] + waterDuration[t]
            for s in range(len(landStartTime)):
                n = max(m, landStartTime[s])
                res = min(res, n + landDuration[s])
        return res