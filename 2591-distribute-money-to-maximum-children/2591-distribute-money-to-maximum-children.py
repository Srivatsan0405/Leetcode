class Solution:
    def distMoney(self, money: int, children: int) -> int:
        money -= children
        if money < 0:
            return -1
        count = min(money // 7, children)
        money -= count * 7
        children -= count
        if children == 0 and money > 0:
            count -= 1

        if children == 1 and money == 3:
            count -= 1
        
        return count