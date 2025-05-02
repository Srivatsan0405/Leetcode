class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        mp = {}
        mp["b"] = 0
        mp["a"] = 0
        mp["l"] = 0
        mp["o"] = 0
        mp["n"] = 0
        
        for txt in text:
            if txt in mp:
                mp[txt] += 1
                
        return min(mp["b"], mp["a"], mp["l"]//2, mp["o"]//2, mp["n"])