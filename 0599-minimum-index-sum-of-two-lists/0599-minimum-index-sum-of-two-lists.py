class Solution:
    def findRestaurant(self, list1, list2):
        m = float('inf')
        res = []
        
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    n = i + j
                    
                    if n < m:
                        m = n
                        res = [list1[i]]  
                    elif n == m:
                        res.append(list1[i])
        
        return res